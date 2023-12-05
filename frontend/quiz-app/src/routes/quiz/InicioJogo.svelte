<script>
	let value;
	import Alert from './Alert.svelte';

	let data = []
	async function handleSubmit(e) {
		if (value <= 0 || value > 10) {
			e.preventDefault();
			localStorage.setItem('jogador', e.nome);
			localStorage.setItem('tema', e.tema);
			localStorage.setItem('qtd', e.qtd);
			data = await load({ url: new URL(window.location.href) });
			console.log(localStorage.getItem('jogador'));
			new Alert({
				target: document.getElementById('alert-container'),
				props: {
					color: 'danger',
					message: 'Selecione um número entre 1 e 10'
				}
			});
		}
	}
</script>

<form action="/" class="my-5" on:submit={handleSubmit}>
	<input
		class="form-control form-control-lg my-3"
		type="number"
		min="0"
		max="10"
		name="qtd"
		bind:value
		placeholder="Número de questões"
	/>
	<input class="form-control my-3 form-control-lg" name="nome" placeholder="Seu nome" />

	<select name="tema" placeholder="Selecione o tema">
		<option value="capitais" selected>Capitais</option>
		<option value="biologia">Biologia</option>
		<option value="quimica">Quimica</option>
		<option value="astronomia">Astronomia</option>
		<option value="geografia">Geografia</option>
		<option value="aleatorio">Aleatorio</option>
	</select>
	<div class="d-grid gap-2">
		<button class="btn btn-success py-4 my-3" type="submit">Start Game</button>
	</div>
</form>
