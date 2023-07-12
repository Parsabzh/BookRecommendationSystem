using booki.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace booki.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly HttpClient _httpClient;

        public HomeController(ILogger<HomeController> logger, HttpClient httpClient)
        {
            _logger = logger;
            _httpClient = httpClient;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> GetText(BookModel book)
        {
            var apiUrl = "http://localhost:105";
            var text = book.GetText;

            var data = await GetDataFromFlaskApi(apiUrl, text);
            return RedirectToAction("ShowResult", new { book = data });
        }

        public IActionResult ShowResult(BookModel book)
        {
            return View(book);
        }


        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }


        public async Task<BookModel?> GetDataFromFlaskApi(string apiUrl, string text)
        {
            var result = new BookModel();

            try
            {
                
                var endpointUrl = $"{apiUrl}/book/{text}";

                var response = await _httpClient.GetAsync(endpointUrl);
                response.EnsureSuccessStatusCode();
                var json = await response.Content.ReadAsStringAsync();
                result = JsonSerializer.Deserialize<BookModel>(json, new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true
                });
                
            }
            catch (HttpRequestException ex)
            {
                if (result != null) result.Message = "Can not access to python";
            }

            return result;
        }
    }
}