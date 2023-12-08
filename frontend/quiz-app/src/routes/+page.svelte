<script>
	export let data;
	import InicioJogo from './quiz/InicioJogo.svelte';
	import Quiz from './quiz/Quiz.svelte';

	let userAnswers = new Array(data.props.length).fill(null);
	let currentScore = 0;
	let currentQuestionIndex = 0;

	console.log(data.props.perguntas);

	function handleAnswerSelect(answerIndex) {
		if (userAnswers[currentQuestionIndex] !== null) {
			return;
		}

		const answer = data.props[currentQuestionIndex].attributes.options[answerIndex];

		if (answer === data.props[currentQuestionIndex].attributes.correct_answer) {
			currentScore++;
		}

		userAnswers[currentQuestionIndex] = answerIndex;
	}

	function nextQuestion() {
		currentQuestionIndex++;
	}
</script>

<section>
	<h1>Quiz - app</h1>
	<div>
		<span> Start Quiz </span>
		{#if !data.props.qtd}
			<InicioJogo />
		{/if}

		{#if data.props.qtd > 0}
			<Quiz
				quizQuestions={data.props.perguntas}
				{currentQuestionIndex}
				{handleAnswerSelect}
				{userAnswers}
			/>

			<div class="flex justify-center mt-4">
				<button
					
					on:click={nextQuestion}
				>
					{currentQuestionIndex !== data.props.qtd ? 'Próximo' : 'Acabou'}
				</button>
			</div>
		{/if}
	</div>
</section>
