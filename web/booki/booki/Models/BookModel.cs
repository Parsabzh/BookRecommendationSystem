namespace booki.Models
{
    public class BookModel
    {
        public BookModel(string name, string isbn, string author, string year, string getText)
        {
            Name = name ?? throw new ArgumentNullException(nameof(name));
            Isbn = isbn ?? throw new ArgumentNullException(nameof(isbn));
            Author = author ?? throw new ArgumentNullException(nameof(author));
            Year = year ?? throw new ArgumentNullException(nameof(year));
            GetText = getText ?? throw new ArgumentNullException(nameof(getText));
        }

        public string Name { get; set; }
        public string Isbn { get; set; }
        public string Author { get; set; }
        public string Year { get; set; }
        public string GetText { get; set; }
    }
}
