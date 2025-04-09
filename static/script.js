fetch('/usuarios')
  .then(res => res.json())
  .then(data => {
    const lista = document.getElementById('usuarios-lista');
    data.forEach(usuario => {
      const li = document.createElement('li');
      li.textContent = `${usuario.nome} - ${usuario.email}`;
      lista.appendChild(li);
    });
  })
  .catch(err => console.error('Erro ao buscar usuários:', err));
