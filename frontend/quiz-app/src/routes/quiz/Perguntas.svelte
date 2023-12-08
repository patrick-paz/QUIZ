<script>

	import CheckmarkIcon from "../../icon/CheckmarkIcon.svelte";
	export let question = [];

	export function handleAnswerSelect(index) {
		userAnswer=index
	}


	export let isAnswered=false;

	export let userAnswer;


	
</script>


<h1>{question.pergunta}</h1>

<div class="flex flex-col gap-2">
	{#each question.respostas as answer, index}
		<button
			class="
            btn btn-outline-primary
			{userAnswer !== null && userAnswer !== undefined
				? answer === question.resposta_correta
					? 'btn btn-outline-success'
					: 'btn btn-outline-danger'
				: 'btn btn-outline-secondary'}"
			on:click={() => handleAnswerSelect(index)}
			disabled={isAnswered}
		>
			{#if userAnswer === index}
				<CheckmarkIcon />
			{/if}
			{answer}
		</button>
	{/each}
</div>
