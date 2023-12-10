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

<div class="flex justify-center mt-4">
	<button class="btn btn-success" on:click={nextQuestion} class:show>
		{currentQuestionIndex + 1 !== quizQuestions.length ? 'Próximo' : 'Acabou'}
	</button>
</div>

<div class="container-fluid border border-light w-100 m-5">
	<p class="text-xs font-light" class:show>
		Tema escolhido: {quizQuestions[currentQuestionIndex]?.tema}
	</p>
	<p class="text-xs font-light" class:show>
		Pergunta {currentQuestionIndex + 1}/{quizQuestions.length}
	</p>

	{#if currentQuestionIndex < quizQuestions.length}

	<div class="container-sm ">
		<h1 class="text-center" >{quizQuestions[currentQuestionIndex].pergunta}</h1>
		<div class="btn-group-vertical w-100 p-3" role="group" aria-label="Vertical button group">
			{#each quizQuestions[currentQuestionIndex].respostas as answer, index}
				<button
					class="
				btn btn-outline-primary p-3 m-2
				{userAnswer !== null && userAnswer !== undefined
						? answer === quizQuestions[currentQuestionIndex].resposta_correta
							? 'btn btn-outline-success'
							: 'btn btn-outline-danger'
						: 'btn btn-outline-secondary'}"
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
</div>
<Modal bind:showNotification>
	{message}
</Modal>

<style>
	.show {
		display: none;
	}

</style>
