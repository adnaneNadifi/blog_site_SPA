declare namespace API {
    type CategoryWithArticles = {
        id:number
        title:string;
        posts: Article
    };

    type Category = {
        id:number
        title:string;
    };

    type Article = {
        id:number,
        title:string;
        content:string;
        categories:Category[];
    };

    type ArticleData = {
        count:number,
        next:string|null,
        previous:string|null,
        results:Article[]
    }


    type CategoryData = {
        count:number,
        next:string|null,
        previous:string|null,
        results:Category[]
    }
  }
  
  