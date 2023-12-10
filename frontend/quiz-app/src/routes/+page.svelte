<script>
	export let data;
	import InicioJogo from './quiz/InicioJogo.svelte';
	import Quiz from './quiz/Quiz.svelte';
</script>

<body class="body full-height">

	<h1>Quiz - app</h1>
	<div class="container bg-dark text-white">

		<div>
			{#if !data.props.qtd}
				<InicioJogo />
			{/if}

			{#if data.props.qtd > 0}
				<Quiz quizQuestions={data.props.perguntas} />
			{/if}
		</div>
	</div>
</body>


<style>
    .body {
        margin: 0;
        padding: 0;
		background-color: black;
		
    }

    .container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh; /* Altura total da janela */
    }

    .full-height {
        height: 100%; /* Altura total da janela */
    }

	h1 {
		text-align: center;
		color: blue;
	}
</style>