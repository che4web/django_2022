<template>
    <div class="container">
        <h2> Создать статью </h2>
        <div>
            <div> Название</div>
            <input v-model="article.name" class="form-control"/>
        </div>

        <div>
            <div> Год</div>
            <input v-model="article.year" class="form-control"/>
        </div>

        <div>
            <div> Описание</div>
            <input v-model="article.description" class="form-control"/>
        </div>

        <div>
            <div> Автор</div>
            <select-author v-model="article.author" />
        </div>

        <div>
            <div> Журнал</div>
            <journal-select v-model="article.journal" />
        </div>

        <div>
            <div> Тип </div>
            <type-select v-model="article.typ2" />
        </div>

        <div v-if="article.typ2 && article.typ2.excentions">
            <div v-for=" ext_field in article.typ2.excentions" :key="ext_field.name">
                <div> {{ext_field.verbose_name}}</div>
                <input v-model="article.addition_info[ext_field.name]" class="form-control"/>
            </div>
        </div>

        <div>
            <div> Тип</div>
            <select v-model="article.typ" class="form-control">
                <option  value="AR"> Статья </option>
                <option value="BK"> Книга </option>
            </select>
        </div>

        <button class="btn btn-primary" @click="save"> Сохранить</button>
    </div>
</template>
<script>
import SelectAuthor from "@/components/SelectAuthor"
import JournalSelect from "@/components/JournalSelect"
import TypeSelect from "@/components/TypeSelect"
import {Article} from "@/api"
export default{
    name:'article-form',
    data(){
        return {
            article:{addition_info:{},}
        }
    },
    components:{
        SelectAuthor,
        JournalSelect,
        TypeSelect,
    },
    methods:{
        async save(){
            let article = {...this.article}
            article.author = [article.author]
            article.typ2 = article.typ2.id

            await Article.objects.save(article)
            this.$router.push('/article/')
        }
    }

}
</script>
