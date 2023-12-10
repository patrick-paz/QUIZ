<script>
	import CheckmarkIcon from '../../icon/CheckmarkIcon.svelte';
	import Pontos from './Pontos.svelte';
	import { corrigirResposta } from '../../lib/functions';
	import Modal from "./Modal.svelte";

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
        console.error("Erro ao corrigir resposta:", error);

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
	<button on:click={nextQuestion} class:show>
		{currentQuestionIndex + 1 !== quizQuestions.length ? 'Próximo' : 'Acabou'}
	</button>
</div>

<div class="bg-white rounded-xl px-4 py-5">
	<p class="text-xs font-light" class:show>
		Pergunta {currentQuestionIndex + 1}/{quizQuestions.length}
	</p>

	{#if currentQuestionIndex < quizQuestions.length}
		<h1>{quizQuestions[currentQuestionIndex].pergunta}</h1>
		<div class="flex flex-col gap-2">
			{#each quizQuestions[currentQuestionIndex].respostas as answer, index}
				<button
					class="
				btn btn-outline-primary
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
					{isAnswered}
				</button>
			{/each}
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
