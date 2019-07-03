using OpenQA.Selenium;
using OpenQA.Selenium.Interactions

public class Test{

	public IWebElement getTransaction_RecurringStartDate_text(){
		return Driver.FindElement(By.id("Transaction_RecurringStartDate"));
	}

	public IWebElement getfirst_name_text(){
		return Driver.FindElement(By.id("first_name"));
	}

	public IWebElement getmiddle_name_text(){
		return Driver.FindElement(By.id("middle_name"));
	}

	public IWebElement getlast_name_text(){
		return Driver.FindElement(By.id("last_name"));
	}

	public IWebElement getaddress_country_text(){
		return Driver.FindElement(By.id("address_country"));
	}

	public IWebElement getaddress_address1_text(){
		return Driver.FindElement(By.id("address_address1"));
	}

	public IWebElement getaddress_address2_text(){
		return Driver.FindElement(By.id("address_address2"));
	}

	public IWebElement getaddress_city_text(){
		return Driver.FindElement(By.id("address_city"));
	}

	public IWebElement getaddress_stateprovince_text(){
		return Driver.FindElement(By.id("address_stateprovince"));
	}

	public IWebElement getaddress_postalcode_text(){
		return Driver.FindElement(By.id("address_postalcode"));
	}

	public IWebElement getaddress_phone_text(){
		return Driver.FindElement(By.id("address_phone"));
	}

	public IWebElement gethonoree_name_text(){
		return Driver.FindElement(By.id("honoree_name"));
	}

	public IWebElement getTransaction_Notification_RecipientName_text(){
		return Driver.FindElement(By.id("Transaction_Notification_RecipientName"));
	}

	public IWebElement getTransaction_Notification_Address_Address1_text(){
		return Driver.FindElement(By.id("Transaction_Notification_Address_Address1"));
	}

	public IWebElement getTransaction_Notification_Address_City_text(){
		return Driver.FindElement(By.id("Transaction_Notification_Address_City"));
	}

	public IWebElement getTransaction_Notification_Address_StateProvince_text(){
		return Driver.FindElement(By.id("Transaction_Notification_Address_StateProvince"));
	}

	public IWebElement getTransaction_Notification_Address_PostalCode_text(){
		return Driver.FindElement(By.id("Transaction_Notification_Address_PostalCode"));
	}

	public IWebElement getTransaction_Notification_Address_Country_text(){
		return Driver.FindElement(By.id("Transaction_Notification_Address_Country"));
	}

	public IWebElement getTransaction_Notification_RecipientName_text(){
		return Driver.FindElement(By.id("Transaction_Notification_RecipientName"));
	}

	public IWebElement getTransaction_Notification_SenderName_text(){
		return Driver.FindElement(By.id("Transaction_Notification_SenderName"));
	}

	public IWebElement getemployerName_text(){
		return Driver.FindElement(By.id("employerName"));
	}

	public IWebElement getfrequency_once_radio(){
		return Driver.FindElement(By.id("frequency_once"));
	}

	public IWebElement getfrequency_monthly_radio(){
		return Driver.FindElement(By.id("frequency_monthly"));
	}

	public IWebElement getfrequency_yearly_radio(){
		return Driver.FindElement(By.id("frequency_yearly"));
	}

	public IWebElement getpayment_credit_radio(){
		return Driver.FindElement(By.id("payment_credit"));
	}

	public IWebElement getpayment_check_radio(){
		return Driver.FindElement(By.id("payment_check"));
	}

	public IWebElement getpayment_paypal_radio(){
		return Driver.FindElement(By.id("payment_paypal"));
	}

	public IWebElement gethonorType_Memory_radio(){
		return Driver.FindElement(By.id("honorType_Memory"));
	}

	public IWebElement gethonorType_InHonorOf_radio(){
		return Driver.FindElement(By.id("honorType_InHonorOf"));
	}

	public IWebElement getnotification_email_radio(){
		return Driver.FindElement(By.id("notification_email"));
	}

	public IWebElement getnotification_card_radio(){
		return Driver.FindElement(By.id("notification_card"));
	}

	public IWebElement getnotification_none_radio(){
		return Driver.FindElement(By.id("notification_none"));
	}

	public IWebElement getcontinue_to_checkout_submit(){
		return Driver.FindElement(By.id("continue_to_checkout"));
	}

}
