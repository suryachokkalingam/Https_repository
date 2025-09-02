import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class SimpleWebServer {
    public static void main(String[] args) throws IOException {
        // Create server listening on port 8081
        HttpServer server = HttpServer.create(new InetSocketAddress("0.0.0.0",8081), 0);

        // Define handler for root path
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                String response = "<h1>Hello, World! 🚀</h1><p>This is my Java web page running on port 8081.</p>";
                exchange.sendResponseHeaders(200, response.getBytes().length);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(response.getBytes());
                }
            }
        });

        // Start server
        server.setExecutor(null); // creates a default executor
        System.out.println("Server running at http://localhost:8081/");
        server.start();
    }
}

