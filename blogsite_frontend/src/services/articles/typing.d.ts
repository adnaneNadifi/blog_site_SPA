declare namespace API {
  type CategoryForm = {
    title: string | null;
  };

  type ArticleForm = {
    title: string | null;
    content: string | null;
    categories: number[];
  };

  type CommentForm = {
    id: number;
    comment: string;
  };

  type CategoryWithArticles = {
    id: number;
    title: string;
    posts: Article;
  };

  type Category = {
    id: number;
    title: string;
  };

  type Article = {
    id: number;
    title: string;
    content: string;
    display_categories: Category[];
    comments: Comment[];
  };

  type ArticleData = {
    count: number;
    next: string | null;
    previous: string | null;
    results: Article[];
  };

  type Comment = {
    comment: string;
  };

  type CategoryData = {
    count: number;
    next: string | null;
    previous: string | null;
    results: Category[];
  };
}
