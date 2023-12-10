<script>
	import CheckmarkIcon from '../../icon/CheckmarkIcon.svelte';
	import { corrigirResposta } from "../../lib/functions";

	export let quizQuestions = [];
	export let currentQuestionIndex = 0;
	export let isAnswered = false;
	export let userAnswer = null;

	console.log(isAnswered); // Está correto aqui, pois é após a declaração e inicialização
	console.log(quizQuestions);

	export function handleAnswerSelect(index, resJogador, resCorreta) {
		userAnswer = index;
		isAnswered = true;

		corrigirResposta(resJogador,resCorreta)
	}

	function nextQuestion() {
		currentQuestionIndex++;
		isAnswered = false;
		userAnswer = null;

		console.log(isAnswered);
	}
</script>

<div class="flex justify-center mt-4">
	<button on:click={nextQuestion}>
		{currentQuestionIndex + 1 !== quizQuestions.length ? 'Próximo' : 'Acabou'}
	</button>
</div>

<div class="bg-white rounded-xl px-4 py-5">
	<p class="text-xs font-light">
		Pergunta {currentQuestionIndex + 1}/{quizQuestions.length}
	</p>

	{#if quizQuestions && Array.isArray(quizQuestions)}
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
					on:click={() => handleAnswerSelect(index, answer, quizQuestions[currentQuestionIndex].resposta_correta)}
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
	{/if}
</div>
