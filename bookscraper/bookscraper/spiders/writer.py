def write_to_file(self):
    with open('payload.txt', 'w') as payload:
        payload.write(book_item["title"])
        payload.write(book_item["price"])
    return 