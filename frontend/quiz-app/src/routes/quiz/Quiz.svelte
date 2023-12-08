<script>
	import Perguntas from './Perguntas.svelte';

	export let quizQuestions = [];
	export let userAnswers = [];
	export let currentQuestionIndex;

	export function handleAnswerSelect(index) {

		userAnswers[currentQuestionIndex] = index;


	}

</script>

<div class="bg-white rounded-xl px-4 py-5">
	<p class="text-xs font-light">
		Pergunta {currentQuestionIndex }/{quizQuestions.length}
	</p>
	<Perguntas
		question={quizQuestions[currentQuestionIndex]}
		{handleAnswerSelect}
		isAnswered={userAnswers[currentQuestionIndex] !== null}
		userAnswer={userAnswers[currentQuestionIndex]}
	/>
</div>
