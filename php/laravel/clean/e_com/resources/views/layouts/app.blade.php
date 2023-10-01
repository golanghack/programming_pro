<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous" />
    <link rel="stylesheet" href="{{ asset('/css/app.css') }}">
    <style>body {background-color: cyan;}</style>
    <title>@yield('title', 'ECom Zoya')</title>
</head>
<body>
    <!--header app-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-secondary py-5">
        <div class="container">
            <a href="#" class="navbar-brand">ZoyaECom</a>
            <button class="navbar-toggler" type="button"
                    data-bs-toggle="collapse"
                    data_bts_target="#navbarNavAltMarkup"
                    aria-controls="navbarNavAltMarkup"
                    aria-expanded="false"
                    aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ms-auto">
                    <a href="#" class="nav-link active">На главную</a>
                    <a href="#" class="nav-link active">О нас</a>
                </div>
            </div>
        </div>
    </nav>
    <header class="masthead bg-primary text-white text-center py-4">
        <div class="container d-flex align-items-center flex-column">
            <h2>@yield('subtitle', 'Онлайн магазин Зои')</h2>
        </div>
    </header>
<!--End header-->
<div class="container my-4">
    @yield('content')
</div>
<!-- footer set-->

    <div class="container">
        <small>
            Copyright - <a class="text-reset fw-bold text-decoration-none" target="_blank"
                    href="https://golanghack.github.io">golanghack</a> - <b>GolangHack</b>
        </small>
    </div>
<!-- end footer -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
</body>
</html>