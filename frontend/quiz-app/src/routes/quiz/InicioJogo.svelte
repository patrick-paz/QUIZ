<script>
	let value;
	import Alert from './Alert.svelte';

	let data = [];
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
<div class='container'>
	<h2>Preencha os dados para começar:</h2>
	<form action="/" on:submit={handleSubmit}>
		<div class="input-form mb-3">
			<input
				class="form-control"
				type="number"
				min="1"
				max="10"
				name="qtd"
				bind:value
				placeholder="Informe o número de questões (entre 1 e 10)"
			/>
		</div>
		<div class="input-form mb-3">
			<input class="form-control" name="nome" placeholder="Seu nome" required />
		</div>
		<div class="input-form mb-3">
			<select class="form-select form-select-sm" name="tema" placeholder="Selecione o tema">
				<option value="capitais" selected>Capitais</option>
				<option value="biologia">Biologia</option>
				<option value="quimica">Quimica</option>
				<option value="astronomia">Astronomia</option>
				<option value="geografia">Geografia</option>
				<option value="aleatorio">Aleatorio</option>
			</select>
		</div>
		<div class="d-grid gap-2 col-6 mx-auto">
			<button class="btn btn-primary" type="submit">Iniciar quiz</button>
		</div>
	</form>
</div>

<style>

.container{
	border: 1;
	border-style: solid;
	border-color: black;
	padding: 65px 65px 65px;
	background-color: #2E2EFE;
}
.input-form{
	width: 75%;
	display: flex;
	flex-direction: column;
	align-items: center;
	margin: auto; 
	height: 100%;
}
h2{
	padding: 10px 10px 10px;
	margin-bottom: 20px;
}
.btn{
	background-color: #FF0000;
	border: 3px;
	border-style: solid;
	border-color: black;
}
button:hover {
  background-color: #B40404;
}
</style>