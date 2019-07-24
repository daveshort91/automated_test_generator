import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Iterator;
import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Test11Test {

private static WebDriver driver = null;

public Test11(WebDriver webdriver){
		driver = webdriver;
	List<WebElement> links = driver.findElements(By.tagName("a"));

	Iterator<WebElement> it = links.iterator();

	url = it.next().getAttribute("href");

	if(url == null || url.isEmpty()){
		System.out.println("URL is either not configured for anchor tag or it is empty");
			continue;}

	huc = (HttpURLConnection)(new URL(url).openConnection());

	huc.setRequestMethod("HEAD");

	huc.connect();

	respCode = huc.getResponseCode();

	if(respCode >= 400){
		System.out.println(url+" is a broken link");
	}
	else{
		System.out.println(url+" is a valid link");
		}
	}
}
