<script>
	export let questions = [];

	console.log(questions);
</script>

{#if questions && questions.length > 0}
	<ul>
		{#each questions as question (question.id)}
			<li>{question.pergunta} -- {question.respostas}</li>
		{/each}
	</ul>
{:else}
	<p>Não há perguntas disponíveis.</p>
{/if}
