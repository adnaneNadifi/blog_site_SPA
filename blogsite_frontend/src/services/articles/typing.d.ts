declare namespace API {
    type Category = {
        id:number
        title:string;
    };

    type Article = {
        id:number
        title:string;
        content:string;
        category:Category;
    };

    type ArticleData = Array<Article>;
    type CategoryData = Array<Category>
  }
  
  