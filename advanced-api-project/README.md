<!-- ## Book Views Documentation

This project includes a set of generic class-based views for managing Book objects.

### List View (`BookListView`)

- Shows all books.
- Publicly accessible.
- Template: `book_list.html`

### Detail View (`BookDetailView`)

- Shows details for a specific book by ID.
- Public access.
- Template: `book_detail.html`

### Create View (`BookCreateView`)

- Allows adding a new book.
- Requires user to be logged in.
- Template: `book_form.html`
- On successful submission, redirects to the list view.
- `form_valid()` method overridden to allow future customization.

### Update View (`BookUpdateView`)

- Allows editing an existing book.
- Login required.
- Shares template with create view.
- `form_valid()` overridden for additional validation/hooks.

### Delete View (`BookDeleteView`)

- Enables deleting a book after confirmation.
- Login required.
- Confirmation template: `book_confirm_delete.html`
- Redirects to list on success.

### Permissions and Authentication

- Create, update, and delete views are protected with `LoginRequiredMixin` to restrict actions to authenticated users.
- List and detail views are public.

### Extensibility

- Override `form_valid()` in create and update views to add additional logic during form submission.
- Customize templates to improve user experience.

This setup utilizes Django's built-in generic views for simplicity and clean code. -->

Book ViewSet Documentation
This project includes a BookViewSet for managing Book objects via an API.

ViewSet (BookViewSet)
Provides full CRUD for Book objects.

Supports listing, retrieving, creating, updating, and deleting.

Uses BookSerializer for JSON serialization.

Permissions
Read (list, retrieve) operations available to everyone.

Write (create, update, delete) operations require login.

Enforced with IsAuthenticatedOrReadOnly.

Endpoints
GET /books/
List all books (public).

GET /books/{id}/
Retrieve book details (public).

POST /books/
Create new book (login required).

PUT /books/{id}/
Update book (login required).

PATCH /books/{id}/
Partial update (login required).

DELETE /books/{id}/
Delete book (login required).
