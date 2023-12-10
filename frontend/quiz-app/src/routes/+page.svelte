<script>
	export let data;
	import InicioJogo from './quiz/InicioJogo.svelte';
	import Quiz from './quiz/Quiz.svelte';





</script>

<section>
	<h1>Quiz - app</h1>
	<div>

		{#if !data.props.qtd}
			<InicioJogo />
		{/if}

		{#if data.props.qtd > 0}
			<Quiz
				quizQuestions={data.props.perguntas}

			/>


		{/if}
	</div>
</section>
