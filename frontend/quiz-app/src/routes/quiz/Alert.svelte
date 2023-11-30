<script>
    export let color, message;
    setTimeout(() => {
        document.querySelector(".alert").remove();
    }, 3000);
</script>

<div class="alert alert-{color}" role="alert">{message}</div>