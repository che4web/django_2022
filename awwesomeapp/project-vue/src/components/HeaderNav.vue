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
                        <a class="nav-link active" aria-current="page" href="{% url 'article_table' %}">Таблица статей</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'article-list'%}">Карточки</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="{% url 'category-list' %}">Стать</a>
                    </li>
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
