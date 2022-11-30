<template>
    <div class="container">
        <a href="/accounts/login" class="btn btn-primary"> админка</a>
    <h2> Таблица статаей</h2> 
    <input id="search" name="search" class="form-control" placeholder="Поиск по названию"  v-model="searchFiedl" >

    <button class="btn btn-primary" onclick="getData()"> поиск</button>

    <div class="row">
        <div class="col-2">
            <h1> фильтры</h1>
            <div>
            выперите автора
            </div>
            <select-author v-model="filters.author"/>

            <div>
            Название
            </div>
            <input v-model="filters.name__icontains" class="form-control"/>

            <div>
            Журнал
            </div>
            <journal-select v-model="filters.journal"/>
        </div>
        <div class="col-10">
<table class="table table-hover ">
    <thead>
        <tr>
            <th> id </th>
            <th> Авторы</th>
            <th @click="setOrdering('name')"> Название </th>
            <th @click="setOrdering('journal')"> Журнал</th>
            <th @click="setOrdering('year')"> Год публикации</th>
            <th> doi </th>
        </tr>
    </thead>
        <tbody >
            <tr v-for="(art,idx) in articleList" :key="art.id" @click="toDetail(art)">
                <td>{{art.id}}</td>
                <td>
                    <div v-for="author in art.author" :key="author.id">{{author.name}}</div>

                </td>
                <td> {{art.name}}</td>
                <td @click.stop="toJournal(art.journal)">{{art.journal? art.journal.name:''}}</td>
                <td>{{art.year}}</td>
                <td>{{art.doi}}</td>
                <td> <button @click="deleteArticel(art,idx)">удалить  </button></td>
                </tr>
        </tbody>
    </table>
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item" :class="activePage==x? 'active':''" v-for="x in maxPage" :key="x" @click="selectPage(x)"><a class="page-link" href="#">{{x}}</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
        </div>

    </div>
    </div>

</template>
<script>
//import axios from 'axios'
import SelectAuthor from "@/components/SelectAuthor"
import JournalSelect  from "@/components/JournalSelect"
import {Article} from "@/api.js"
export default{
    name:'article-table',
   data(){
        return {
            filters:{},
            searchFiedl:'',
            selectAuthor:{},
            maxPage:1,
            activePage:1,
            articleList:[
            ]
        }
    },
    components:{
        SelectAuthor,
        JournalSelect,
    },
    watch:{
        searchFiedl(){
            this.getArticle()
        },
        filters:{
            deep:true,
            handler(){
                this.getArticle()
            },
        },
    },
    mounted(){
        this.getArticle()
    },
    methods:{
        selectPage(p){
            this.activePage=p
            this.getArticle()
        },
        toJournal(journal){
            this.$router.push({name:'journal-detail',params:{id:journal.id}})
        },
        toDetail(art){
            this.$router.push({name:'article-detail',params:{id:art.id}})
        },
        async deleteArticel(art,idx){
            await Article.objects.delete(art)
            this.articleList.splice(idx,1)
        },
        setOrdering(filed_name){
            this.filters.ordering = this.filters.ordering==filed_name? '-'+filed_name: filed_name
        },
        updateAutho(event){
            this.filters['author']=event.id
        },
        async getArticle(){
            //let   params={
            //    author__name__icontains:this.searchFiedl,
            //    author:this.selectAuthor.id
           // }
            let params = {...this.filters,page:this.activePage}
            params['journal'] = this.filters.journal? this.filters.journal.id:undefined
            params['author'] = this.filters.author? this.filters.author.id:undefined
            let response = await Article.objects.filter(params)
            this.maxPage = response.total_pages
            //let data =  (await axios.get('/api/article/',{params})).data
            this.articleList = response.results
        }
    },

}
</script>
