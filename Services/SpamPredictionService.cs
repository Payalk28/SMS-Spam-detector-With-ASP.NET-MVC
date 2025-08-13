using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace SpamClassifierWebApp.Services
{
    public class SpamPredictionService
    {
        // This class is a good practice for dependency injection and managing
        // HTTP client instances.
        private readonly HttpClient _httpClient;

        // Constructor for dependency injection
        public SpamPredictionService(HttpClient httpClient)
        {
            _httpClient = httpClient;
            // Configure the base address of your Python API
            // Make sure this matches the port from app.py
            _httpClient.BaseAddress = new Uri("http://localhost:5000/");
        }

        // Helper class to deserialize the JSON response from Python API
        private class SpamPredictionResponse
        {
            public string? Prediction { get; set; }
        }

        public async Task<string> GetSpamPredictionAsync(string message)
        {
            // Prepare the data to be sent as JSON
            var requestData = new { message = message };
            var jsonContent = JsonSerializer.Serialize(requestData);
            var httpContent = new StringContent(jsonContent, Encoding.UTF8, "application/json");

            try
            {
                // Send the POST request to the Python API's /predict endpoint
                HttpResponseMessage response = await _httpClient.PostAsync("predict", httpContent);

                response.EnsureSuccessStatusCode(); // Throws an exception for HTTP error codes

                // Read the response content as a string
                string responseBody = await response.Content.ReadAsStringAsync();

                // Deserialize the JSON response
                var predictionResult = JsonSerializer.Deserialize<SpamPredictionResponse>(responseBody);

                // Return the prediction
                return predictionResult?.Prediction ?? "unknown";
            }
            catch (HttpRequestException e)
            {
                // Log and handle network or API-related errors
                // In a production app, you would log this error.
                Console.WriteLine($"Request error: {e.Message}");
                return "Error contacting prediction service.";
            }
            catch (JsonException e)
            {
                // Log and handle JSON deserialization errors
                Console.WriteLine($"JSON deserialization error: {e.Message}");
                return "Error processing prediction result.";
            }
        }
    }
}
