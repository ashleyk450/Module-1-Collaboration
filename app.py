from flask import Flask, jsonify, request

app = Flask(__name__)

books = []

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET single book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"})

# CREATE book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        "id": len(books) + 1,
        "book_name": request.json["book_name"],
        "author": request.json["author"],
        "publisher": request.json["publisher"]
    }
    books.append(new_book)
    return jsonify(new_book)

# UPDATE book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book["id"] == id:
            book["book_name"] = request.json["book_name"]
            book["author"] = request.json["author"]
            book["publisher"] = request.json["publisher"]
            return jsonify(book)
    return jsonify({"message": "Book not found"})

# DELETE book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"})

if __name__ == '__main__':
    app.run(debug=True)
    