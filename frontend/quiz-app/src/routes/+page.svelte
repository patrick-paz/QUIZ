<script>
	export let data;
	import InicioJogo from './quiz/InicioJogo.svelte';
	import Quiz from './quiz/Quiz.svelte';
</script>

<body class="body full-height">
	<div class='container'>
		<h1>Quiz - app</h1>
		<div class="container text-white">
			
			<div>
				{#if !data.props.qtd}
					<InicioJogo />
				{/if}

				{#if data.props.qtd > 0}
					<Quiz quizQuestions={data.props.perguntas} />
				{/if}
			</div>
		</div>
	</div>
</body>


<style>
    .body {
        margin: 0;
        padding: 0;	
		background: url('https://img.freepik.com/premium-vector/vector-seamless-pattern-question-marks-quiz-background_574806-1824.jpg');	
    }

    .container {
        display: flex;
        align-items: center;
        height: 100vh; 
		flex-direction: column; 
        justify-content: flex-start;
    }

    .full-height {
        height: 100%;
    }

	h1 {
		text-align: center;
		color:#2E2EFE;
		margin-bottom: 30px; 
		margin-top: 65px; 
	}
</style>