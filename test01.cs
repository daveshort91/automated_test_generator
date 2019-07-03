using OpenQA.Selenium;
using OpenQA.Selenium.Interactions

public class Test{

public IWebElement getTransaction_RecurringStartDateText(){
return Driver.FindElement(By.id("Transaction_RecurringStartDate"));
}

public IWebElement getfirst-nameText(){
return Driver.FindElement(By.id("first-name"));
}

public IWebElement getmiddle-nameText(){
return Driver.FindElement(By.id("middle-name"));
}

public IWebElement getlast-nameText(){
return Driver.FindElement(By.id("last-name"));
}

public IWebElement getaddress-countryText(){
return Driver.FindElement(By.id("address-country"));
}

public IWebElement getaddress-address1Text(){
return Driver.FindElement(By.id("address-address1"));
}

public IWebElement getaddress-address2Text(){
return Driver.FindElement(By.id("address-address2"));
}

public IWebElement getaddress_cityText(){
return Driver.FindElement(By.id("address_city"));
}

public IWebElement getaddress-stateprovinceText(){
return Driver.FindElement(By.id("address-stateprovince"));
}

public IWebElement getaddress-postalcodeText(){
return Driver.FindElement(By.id("address-postalcode"));
}

public IWebElement getaddress-phoneText(){
return Driver.FindElement(By.id("address-phone"));
}

public IWebElement gethonoree-nameText(){
return Driver.FindElement(By.id("honoree-name"));
}

public IWebElement getTransaction_Notification_RecipientNameText(){
return Driver.FindElement(By.id("Transaction_Notification_RecipientName"));
}

public IWebElement getTransaction_Notification_Address_Address1Text(){
return Driver.FindElement(By.id("Transaction_Notification_Address_Address1"));
}

public IWebElement getTransaction_Notification_Address_CityText(){
return Driver.FindElement(By.id("Transaction_Notification_Address_City"));
}

public IWebElement getTransaction_Notification_Address_StateProvinceText(){
return Driver.FindElement(By.id("Transaction_Notification_Address_StateProvince"));
}

public IWebElement getTransaction_Notification_Address_PostalCodeText(){
return Driver.FindElement(By.id("Transaction_Notification_Address_PostalCode"));
}

public IWebElement getTransaction_Notification_Address_CountryText(){
return Driver.FindElement(By.id("Transaction_Notification_Address_Country"));
}

public IWebElement getTransaction_Notification_RecipientNameText(){
return Driver.FindElement(By.id("Transaction_Notification_RecipientName"));
}

public IWebElement getTransaction_Notification_SenderNameText(){
return Driver.FindElement(By.id("Transaction_Notification_SenderName"));
}

public IWebElement getemployerNameText(){
return Driver.FindElement(By.id("employerName"));
}

public IWebElement getfrequency_onceRadio(){
return Driver.FindElement(By.id("frequency_once"));
}

public IWebElement getfrequency_monthlyRadio(){
return Driver.FindElement(By.id("frequency_monthly"));
}

public IWebElement getfrequency_yearlyRadio(){
return Driver.FindElement(By.id("frequency_yearly"));
}

public IWebElement getpayment_creditRadio(){
return Driver.FindElement(By.id("payment_credit"));
}

public IWebElement getpayment_checkRadio(){
return Driver.FindElement(By.id("payment_check"));
}

public IWebElement getpayment_paypalRadio(){
return Driver.FindElement(By.id("payment_paypal"));
}

public IWebElement gethonorType_MemoryRadio(){
return Driver.FindElement(By.id("honorType_Memory"));
}

public IWebElement gethonorType_InHonorOfRadio(){
return Driver.FindElement(By.id("honorType_InHonorOf"));
}

public IWebElement getnotification_emailRadio(){
return Driver.FindElement(By.id("notification_email"));
}

public IWebElement getnotification_cardRadio(){
return Driver.FindElement(By.id("notification_card"));
}

public IWebElement getnotification_noneRadio(){
return Driver.FindElement(By.id("notification_none"));
}

public IWebElement getcontinue-to-checkoutSubmit(){
return Driver.FindElement(By.id("continue-to-checkout"));
}

}
