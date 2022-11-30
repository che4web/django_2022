<template>
    <div class="container">
        <div>
            <div> Название</div>
            <input v-model="article.name"/>
        </div>

        <div>
            <div> Год</div>
            <input v-model="article.year"/>
        </div>

        <div>
            <div> Тип</div>
            <select v-model="article.type">
                <option  value="AR"> Статья </option>
                <option value="BK"> Книга </option>
            </select>
        </div>

        <div class="book_form" v-if="article.type=='BK'">

            <div>
                <div> Издатель</div>
                <input v-model="article.publisher"/>
            </div>
        </div>

        <div class="article_form" v-if="article.type=='AR'">
            <div>
                <div> Журнал</div>
                <input v-model="article.journal"/>
                <h2> все что угодно </h2>
            </div>

            <div>
                <div> Ипакт фактор</div>
                <input v-model="article.foo"/>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    name:'article-form',
    data(){
        return {
            article:{}
        }
    }

}
</script>
