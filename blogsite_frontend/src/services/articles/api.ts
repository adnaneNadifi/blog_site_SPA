import axiosInterceptor from 'src/utils/axiosInterceptor';

export const getArticles = (pageUrl:string|null) => {

  let apiUrl = `/api/blog_posts/`;

  if(pageUrl !== null){
    apiUrl = pageUrl;
  }

  return axiosInterceptor.get<API.ArticleData>(
    apiUrl,
  );
};


export const getArticle = (articleId:number) => {
  return axiosInterceptor.get<API.Article>(
    `api/blog_posts/${articleId}`,
  );
};

export const getCategories = () => {
  return axiosInterceptor.get<API.CategoryData>(
    '/api/categories/',
  );
};

export const getCategoryWithArticles = (categoryId: number) => {
  return axiosInterceptor.get<API.CategoryWithArticles>(
    `/api/categories/${categoryId}`,
  )
}