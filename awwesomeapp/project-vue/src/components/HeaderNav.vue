<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container">
            <a class="navbar-brand" href="#"> Che Art</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article/">Статьи</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article/my">Мои статьи</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article/form">Создать статью</router-link>
                    </li>
                    <li class="nav-item">
                        <a   class="nav-link "  href="/admin" > админка</a>
                    </li >
                </ul>
                <span class="navbar-text">
                </span>
            </div>
        </div>
    </nav>

</template>
<script>
export default{
    name:'header-nav'
}
</script>
