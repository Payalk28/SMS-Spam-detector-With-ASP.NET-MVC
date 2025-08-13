using Microsoft.AspNetCore.Mvc;
using SpamClassifierWebApp.Services;
using System.Threading.Tasks;

namespace SpamClassifierWebApp.Controllers
{
    public class SpamController : Controller
    {
        private readonly SpamPredictionService _spamPredictionService;

        // The service is injected by ASP.NET Core's dependency injection system
        public SpamController(SpamPredictionService spamPredictionService)
        {
            _spamPredictionService = spamPredictionService;
        }

        // This action handles the initial page load and displays the form.
        public IActionResult Index()
        {
            return View();
        }

        // This action is a backend API endpoint that the frontend will call via AJAX.
        // It receives the message and returns the prediction as JSON.
        [HttpPost]
        public async Task<IActionResult> ClassifyMessage([FromBody] string message)
        {
            if (string.IsNullOrWhiteSpace(message))
            {
                return BadRequest(new { error = "Message cannot be empty." });
            }

            string prediction = await _spamPredictionService.GetSpamPredictionAsync(message);

            // Return the prediction as a JSON object
            return Ok(new { prediction = prediction });
        }
    }
}
