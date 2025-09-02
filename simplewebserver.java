import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class SimpleWebServer {
    public static void main(String[] args) throws IOException {
        // Create server listening on port 8080
        HttpServer server = HttpServer.create(new InetSocketAddress(8081), 0);

        // Define handler for root path
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                String response = "<h1>Hello, World! 🚀</h1><p>This is my Java web page.</p>";
                exchange.sendResponseHeaders(200, response.getBytes().length);
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
                os.close();
            }
        });

        // Start server
        server.setExecutor(null);
        System.out.println("Server running at http://localhost:8080/");
        server.start();
    }
}

