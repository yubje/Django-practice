# README



Django skeleton code

## 1. accounts

* `signup`

* `login`
* `logout`

## 2. community

* `index`(`review_list`) : List of posts 
* `create` : New post
* `detail`(`review_detail`) : Post in detail
* `update` 
  * Editing a post.
  * Only possible for the user who created the post.
  * Redirects to detail page
* `delete` 
  * Deleting a post.
  * Only possible for the user who created the post.
  * Redirects to index(`review_list`) page
* `create comment`(`comments_create`) 
  * Writing a comment.
  * Only possible for the authenticated user.
  * Redirects to login page if the user is not authenticated.
* `delete comment`(` comments_delete`)
  * Deleting a comment.
  * Only possible for the user who created the comment.
  * Redirects to login page if the user is not authenticated

## TBU

> edit comment, edit account information 