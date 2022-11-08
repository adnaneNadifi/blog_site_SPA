import axiosInterceptor from 'src/utils/axiosInterceptor';

export const getArticles = () => {
  return axiosInterceptor.get<API.ArticleData>(
    '/api/blog_posts/',
  );
};

export const getCategories = () => {
  return axiosInterceptor.get<API.CategoryData>(
    '/api/categories/',
  );
};
