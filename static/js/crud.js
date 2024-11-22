// Captura todos os botões de deletar

document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            event.preventDefault();

            const comentarioId = button.dataset.id;

            // Confirmação antes de excluir
            if (!confirm('Tem certeza que deseja excluir este comentário?')) {
                return;
            }

            try {
                // Enviar requisição DELETE para o backend
                const response = await fetch(`/receitas/${comentarioId}/delete`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });

                // Checar se a requisição foi bem-sucedida
                if (response.ok) {
                    const result = await response.json();

                    if (result.deleted === 'ok') {
                        // Remover o card do DOM
                        const card = document.getElementById(`comentario-card-${comentarioId}`);
                        if (card) {
                            card.remove();
                        }
                        alert('Comentário deletado com sucesso!');
                    } else {
                        alert('Erro ao deletar comentário. Tente novamente.');
                    }
                } else {
                    alert('Erro na requisição. Verifique o servidor.');
                }
            } catch (error) {
                console.error('Erro ao deletar o comentário:', error);
                alert('Ocorreu um erro. Tente novamente mais tarde.');
            }
        });
    });
});

