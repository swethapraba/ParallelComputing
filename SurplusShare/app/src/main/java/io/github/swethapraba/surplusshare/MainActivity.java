package io.github.swethapraba.surplusshare;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    public final static String EXTRA_MESSAGE = "io.github.swethapraba.surplusshare.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void sendMessageDonate(View view)
    {
        //Do something in response to the button
        Intent intentD = new Intent(this, FindLocations.class);
        String message = "donor";
        intentD.putExtra(EXTRA_MESSAGE, message);
        startActivity(intentD);
    }


    public void sendMessageAccept(View view)
    {
        //Do something in response to the button
        Intent intentA = new Intent(this, FindDonors.class);
        String message = "location";
        intentA.putExtra(EXTRA_MESSAGE, message);
        startActivity(intentA);
    }

    public void aboutSurplusShare(View view)
    {
        //Do something in response to the button
        Intent intentS = new Intent(this, AboutSurplusShare.class);
        String message = "about";
        intentS.putExtra(EXTRA_MESSAGE, message);
        startActivity(intentS);
    }
}
