<script>
	import CheckmarkIcon from '../../icon/CheckmarkIcon.svelte';
	import Pontos from './Pontos.svelte';
	import { corrigirResposta } from '../../lib/functions';
	import Modal from './Modal.svelte';

	export let quizQuestions = [];
	export let currentQuestionIndex = 0;
	export let isAnswered = false;
	export let userAnswer = null;
	let show = false;
	let showNotification = false;
	let message = '';

	console.log(isAnswered); // Está correto aqui, pois é após a declaração e inicialização
	console.log(quizQuestions);

	export async function handleAnswerSelect(index, resJogador, resCorreta) {
		userAnswer = index;
		isAnswered = true;

		try {
			const notificationMessage = await corrigirResposta(resJogador, resCorreta);

			console.log(notificationMessage);

			showNotification = true;
			message = notificationMessage;
		} catch (error) {
			console.error('Erro ao corrigir resposta:', error);
		}
	}

	function nextQuestion() {
		currentQuestionIndex++;
		isAnswered = false;
		userAnswer = null;
		if (currentQuestionIndex == quizQuestions.length) {
			show = !show;
		}
		console.log(isAnswered);
	}
</script>

<div class="button">
	<button class="scs btn-success" on:click={nextQuestion} class:show>
		{currentQuestionIndex + 1 !== quizQuestions.length ? 'Próximo' : 'Finalizar'}
	</button>
</div>

<!-- <div class="container-fluid border border-light w-100 m-5"> -->

{#if currentQuestionIndex < quizQuestions.length}
	<div class="container-sm">
		<p class="text-xs font-light" class:show>
			Tema escolhido: {quizQuestions[currentQuestionIndex]?.tema}
		</p>
		<p class="text-xs font-light" class:show>
			Pergunta {currentQuestionIndex + 1}/{quizQuestions.length}
		</p>
		<h1 class="text-center">{quizQuestions[currentQuestionIndex].pergunta}</h1>
		<div class="btn-group-vertical w-50 p-3" role="group" aria-label="Vertical button group">
			{#each quizQuestions[currentQuestionIndex].respostas as answer, index}
				<button
					class="
				btn btn-primary p-3 m-2
				{userAnswer !== null && userAnswer !== undefined
						? answer === quizQuestions[currentQuestionIndex].resposta_correta
							? 'btn btn-success'
							: 'btn btn-danger'
						: 'btn btn-secondary'}"
					on:click={() =>
						handleAnswerSelect(index, answer, quizQuestions[currentQuestionIndex].resposta_correta)}
					disabled={isAnswered}
				>
					{#if userAnswer === index}
						<CheckmarkIcon />
					{/if}
					{answer}
				</button>
			{/each}
		</div>
	</div>
{:else}
	<Pontos qtdTotal={quizQuestions.length} />
{/if}
<!-- </div> -->
<Modal bind:showNotification>
	{message}
</Modal>

<style>
	.show {
		display: none;
	}
	.text-center{
		font-size: 20px;
	}
	.container-sm {
		border: 1;
		border-style: solid;
		border-color: black;
		padding: 35px 35px 35px;
		background-color: #2E2EFE;
	}
	.button {
		margin-bottom: 10px;
	}
	.btn{
		border: 2px;
		border-style: solid;
		border-color: black;
		width: 300px;
		font-size: 15px;
		font-weight: bolder;
	}

	.scs {
		border: 2px;
		border-style: solid;
		border-color: black;
		width: 150px;
	}
	.btn-group-vertical {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: auto; 
	}

	.btn-group-vertical .btn {
		margin-bottom: 5px; 
	}
</style>
