import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;

public class StepImplementation extends BaseTest {


    @Step("<key> id li elemente tıkla")
    public void clickBYid(String key) throws InterruptedException {
        By.id(key).findElement(appiumDriver).click();
        Thread.sleep(3000);
    }

    @Step("<key> id li elemente <text>  değerini yaz")
    public void sendkeyBYid(String key, String text) {
        appiumDriver.findElement(By.id(key)).sendKeys(text);
    }

    @Step("<key> xpath li elemente tıkla")
    public void clickBYxpath(String key) {
        appiumDriver.findElement(By.xpath(key)).click();
    }

    @Step("<key> css elementine tıkla ")
    public void clickEl(String key){
        appiumDriver.findElement(By.cssSelector(key)).click();
    }

    @Step("<number> saniye bekle")
    public void waitForSeceond(int number) throws InterruptedException {
        Thread.sleep(number * 1000);
    }

    @Step("<key> id li element <text> değerini  içerdiğini kontrol et")
    public void CheckElement(String key, String text) {
        Assert.assertFalse(appiumDriver.findElement(By.id(key)).getText().equals(text));
    }
}
