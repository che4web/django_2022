<template>
    <div class="container">
        <a href="/accounts/login" class="btn btn-primary"> админка</a>
    <h2> Таблица моих статей статаей</h2> 
    <input id="search" name="search" class="form-control" placeholder="Поиск по названию"  v-model="searchFiedl" >

    <button class="btn btn-primary" onclick="getData()"> поиск</button>
<table class="table table-hover ">
    <thead>
        <tr>
            <th> id </th>
            <th> Название </th>
            <th> Авторы</th>
            <th> Журнал</th>
            <th> Год публикации</th>
            <th> doi </th>
        </tr>
    </thead>
        <tbody >
            <tr v-for="art in articleList" :key="art.id">
                <td>{{art.id}}</td>
                <td> {{art.name}}</td>
                <td>
                    <div v-for="author in art.author" :key="author.id">{{author.name}}</div>

                </td>
                <td>{{art.journal? art.journal.name:''}}</td>
                <td>{{art.year}}</td>
                <td>{{art.doi}}</td>
                </tr>
        </tbody>
    </table>
    </div>

</template>
<script>
import {Article,Author} from "@/api.js"
export default{
    name:'article-table',
   data(){
        return {
            searchFiedl:'',
            selectAuthor:{},
            articleList:[
            ]
        }
    },
    components:{
    },
    watch:{
        searchFiedl(){
            this.getArticle()
        },
        selectAuthor(){
            this.getArticle()
        },
    },
    mounted(){
        this.getArticle()
    },
    methods:{
        updateAutho(event){
            this.selectAuthor=event
        },
        async getArticle(){
            let author  = await  Author.objects.who_iam()
            let   params={
                author__name__icontains:this.searchFiedl,
                author:author.id
            }
            //let data =  (await axios.get('/api/article/my_article/',{params})).data
            let data =  await Article.objects.filter(params)
            this.articleList = data
        }
    },

}
</script>
