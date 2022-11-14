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

export const addArticle = (article:object)=>{
  return axiosInterceptor.post<API.Article>(
    `api/blog_posts/`,article
  );
}

export const getCategories = (pageUrl:string|null) => {
  
  let  apiUrl ='/api/categories/'
  if ( pageUrl !== null ) {
    apiUrl = pageUrl
  }

  return axiosInterceptor.get<API.CategoryData>(
    apiUrl,
  );
};

export const getAllCategories = ()=>{
  return axiosInterceptor.get<API.Category[]>(
    `api/all_categories/`,
  );
}

export const getCategoryWithArticles = (categoryId: number) => {
  return axiosInterceptor.get<API.CategoryWithArticles>(
    `/api/categories/${categoryId}`,
  )
}

export const addCategory = (category:object) => {
  return axiosInterceptor.post(
    '/api/add_category/',category
  );
};

export const deletCategory = (id:number) => {
  return axiosInterceptor.delete(
    `/api/categories_delete/${id}`,
  );
};

export const updateCategory = (id:number,category:object) => {
  return axiosInterceptor.patch(
    `/api/categories_update/${id}`,category
  );
};

export const addComment = (comment:API.CommentForm) => {
  return axiosInterceptor.post<API.Comment>(
    '/api/posts_comment/',comment
  );
}