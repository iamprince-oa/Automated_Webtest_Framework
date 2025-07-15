describe('MTN Ghana Website Contact Flow', function () {
    it('should navigate to contact page and submit callback request', function () {
        browser.url('https://mtn.com.gh/');
        browser.setTimeout({ implicit: 10000 });

        // Try closing cookie popup
        try {
            const popupClose = $('.cky-banner-btn-close');
            if (popupClose.isDisplayed()) {
                popupClose.click();
                console.log('Pop-Up Closed');
            }
        } catch (e) {
            console.log('Pop-Up Not Found');
        }

        // Navigate to Business section
        const businessLink = $('=BUSINESS');
        businessLink.click();

        // Read heading text
        const heading = $('.yello-heading');
        console.log(heading.getText());

        // Navigate to Contact page
        const contactLink = $('=Contact');
        contactLink.click();

        // Fill out contact form
        $('[name="vwp-first-name"]').setValue('Prince');
        $('[name="vwp-surname"]').setValue('Owusu');
        $('[name="vwp-contact-number"]').setValue('0593130530');
        $('[name="vwp-email-address"]').setValue('owusup484@gmail.com');
        $('[name="vwp-business-name"]').setValue('MTN-Ghana-Attachment');

        // Pause for manual reCAPTCHA completion
        browser.pause(30000); // or input() flow handled externally

        // Verify reCAPTCHA
        $('#recaptcha-verify-button').click();

        // Submit callback request
        $('.mtn-callback-form-btn').click();

        console.log('Test Completed and Successful');
    });
});
