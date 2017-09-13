package io.github.swethapraba.surplusshare;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.app.NotificationCompat;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class FindLocations extends AppCompatActivity
{
    String[][] loudoun =
    {
           /* {Name,Address, Phone Number,Website,
               M-F Open,M-F Close,Sat Open,Sat Close,Sun Open,Sun Close,Special Instructions, Special Requests,
                    Fresh,Cooked,Boxed,Canned,Frozen,Packaged(e.g.EasyMac)},*/

            {"Loudoun Interfaith Relief", "750 Miller Drive, Suite A-1 Leesburg, VA, 20175", "703-777-5911","www.interfaithrelief.org",
            "9:30","16:00","9:00","13:00","0:00","0:00","None", "Granola Bars, Fruit Cups, Popcorn, Nutrition Shakes, Infant Cereal, Peanut Butter",
            "Y","N","Y","Y","N","Y"},
            /* {"Messiah's Market at Community Church",Address, Phone Number,Website,
               M-F Open,M-F Close,Sat Open,Sat Close,Sun Open,Sun Close,Special Instructions, Special Requests,
                    Fresh,Cooked,Boxed,Canned,Frozen,Packaged(e.g.EasyMac)},*/

            {"Seven Loaves Services", "15 W. Washington Street Middleburg, VA 20117", "540-687-3489","www.sevenloavesmiddleburg.org",
                    "10:00", "12:00","0:00","0:00","0:00","0:00","Closed Tuesdays and Thursdays", "Eggs,Pasta/Pasta Sauces,Beans,Rice,Canned Tuna",
                    "Y","N","Y","Y","Y","Y"},

            {"Tree of Life Food Pantry", "Dropoff locations listed on website", "703-554-3595","www.tolministries.org",
                    "9:00","14:00","0:00","0:00","0:00","0:00","None","Jelly,Breakfast Items,Peanut Butter,Baking Items,Dry Milk,Honey,Cake Mixes/Frosting",
                    "N","N","Y","Y","N","Y"}
    };
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_find_locations);

        Intent intent = getIntent();
        String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);
        System.out.println(message);

        final Button button = (Button) findViewById(R.id.dropoffSearch);
        button.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v)
            {
                // Perform action on click
                String unit = "boxes";
                int cat;
                EditText editText1 = (EditText) findViewById(R.id.category);
                String foodCategory = editText1.getText().toString();
                if(foodCategory.equalsIgnoreCase("fresh"))
                {
                    cat = 12;
                }
                else if(foodCategory.equalsIgnoreCase("cooked"))
                {
                    cat = 13;
                }
                else if (foodCategory.equalsIgnoreCase("boxed"))
                {
                    cat = 14;
                }
                else if (foodCategory.equals("canned"))
                {
                    cat = 15;
                }
                else if (foodCategory.equalsIgnoreCase("frozen"))
                {
                    cat = 16;
                }
                else
                {
                    cat = 17;
                }

                EditText editText2 = (EditText) findViewById(R.id.food);
                String foodName = editText2.getText().toString();

                EditText editText3 = (EditText) findViewById(R.id.quantity);
                String foodQuantity = editText3.getText().toString();

                CheckBox checkBox1 = (CheckBox) findViewById(R.id.servings);
                boolean isServings = checkBox1.isChecked();
                if(isServings)
                {
                    unit = "servings";
                }
                CheckBox checkBox2 = (CheckBox) findViewById(R.id.ozs);
                boolean isOunces = checkBox2.isChecked();
                if(isOunces)
                {
                    unit = "oz";
                }
                CheckBox checkBox3 = (CheckBox) findViewById(R.id.lbs);
                boolean isPounds = checkBox3.isChecked();
                if(isPounds)
                {
                    unit = "lbs";
                }
                CheckBox checkBox4 = (CheckBox) findViewById(R.id.packages);
                boolean isPackages = checkBox4.isChecked();
                if(isPackages)
                {
                    unit = "packages";
                }

                //Set up for adding results
                String noResults = "It doesn't look like any location in our database can accept your food.";
                String myResults = "";
                boolean resultview = false;
                //Firebase stuff to match results
                //mDatabase = FirebaseDatabase.getInstance().getReference();
                //look for the category
                //check special requests of each person for the food name
                //if yes, in results display: name, address, phone number, website, special instructions, hours
                for(int x = 0; x < loudoun.length;x++)
                {
                    String accepts = loudoun[x][cat];
                    if(accepts.equalsIgnoreCase("y"))
                    {
                        resultview = true;
                        myResults+= loudoun[x][0] /*name*/ + "\n" + loudoun[x][1] /*address*/ + "\n" + loudoun[x][2] /*phone*/ + "  | " + loudoun[x][3] /*website*/ + "\n";

                        int mfoint = Integer.parseInt(loudoun[x][4].substring(0,1));
                        if(mfoint !=0)
                        {
                            String r = loudoun[x][4];
                            String[] p = r.split(":");
                            int t = 12 - Integer.parseInt(p[0]);
                            if(t<0)
                            {
                                String MFO = (t*-1)+"";
                                myResults+= "M-F Open: " + MFO +" PM  ";
                            }
                            else if(t>0) {myResults += "M-F Open: " + p[0] +" AM  | ";}
                            else if(t==0) {myResults+= "M-F Open: Noon  | ";}
                            /****/
                            String rt = loudoun[x][5];
                            String[] pt = rt.split(":");
                            int tt = 12 - Integer.parseInt(pt[0]);
                            if(tt<0)
                            {
                                String MFC = (tt*-1)+"";
                                myResults+= "Close: " + MFC +" PM \n";
                            }
                            else if(tt>0) {myResults += "Close: " + pt[0] +" AM \n";}
                            else if(tt==0) {myResults+= "Close: Noon \n";}
                        }

                        int saoint = Integer.parseInt(loudoun[x][6].substring(0,1));
                        if(saoint !=0)
                        {
                            String r = loudoun[x][6];
                            String[] p = r.split(":");
                            int t = 12 - Integer.parseInt(p[0]);
                            if(t<0)
                            {
                                String SAO = (t*-1)+"";
                                myResults+= "Sat Open: " + SAO +" PM ";
                            }
                            else if(t>0) {myResults += "Sat Open: " + p[0] +" AM | ";}
                            else if(t==0) {myResults+= "Sat Open: Noon | ";}
                            /***/
                            String rt = loudoun[x][7];
                            String[] pt = rt.split(":");
                            int tt = 12 - Integer.parseInt(pt[0]);
                            if(tt<0)
                            {
                                String SAC = (tt*-1)+"";
                                myResults+= "Close: " + SAC +" PM \n";
                            }
                            else if(tt>0) {myResults += "Close: " + pt[0] +" AM \n";}
                            else if(tt==0) {myResults+= "Close: Noon \n";}
                        }

                        int suoint = Integer.parseInt(loudoun[x][8].substring(0,1));
                        if(suoint !=0)
                        {
                            String r = loudoun[x][8];
                            String[] p = r.split(":");
                            int t = 12 - Integer.parseInt(p[0]);
                            if(t<0)
                            {
                                String SUO = (t*-1)+"";
                                myResults+= "Sun Open: " + SUO +" PM | ";
                            }
                            else if(t>0) {myResults += "Sun Open: " + p[0] +" AM | ";}
                            else if(t==0) {myResults+= "Sun Open: Noon | ";}
                            /***/
                            String rt = loudoun[x][9];
                            String[] pt = rt.split(":");
                            int tt = 12 - Integer.parseInt(pt[0]);
                            if(tt<0)
                            {
                                String SUC = (tt*-1)+"";
                                myResults+= "Close: " + SUC +" PM + \n";
                            }
                            else if(tt>0) {myResults += "Close: " + pt[0] +" AM \n";}
                            else if(tt==0) {myResults+= "Close: Noon \n";}
                        }
                        if(!(loudoun[x][10]).equalsIgnoreCase("none"))
                            myResults+= "Notes: " + loudoun[x][10] + "\n";
                        myResults += "***************************************** \n";
                    }
                }

                if(!resultview)
                {
                    myResults = noResults;
                }

                createNewTextView(myResults,foodQuantity,unit,foodName);
            }
        });
    }
    public void createNewTextView(String text,String foodQ, String units,String foodN)
    {
        //Add results
        TextView textView = new TextView(this);
        textView.setTextSize(15);
        textView.setText(text);
        RelativeLayout layout = (RelativeLayout) findViewById(R.id.results);
        layout.addView(textView);

        //send a notification
        NotificationCompat.Builder mBuilder =
                (NotificationCompat.Builder) new NotificationCompat.Builder(this).setSmallIcon(R.drawable.notification_icon)
                        .setContentTitle("SurplusShare").setContentText("Don't forget to drop off your " + foodQ + " " + units + " of " + foodN + "!");
        Intent resultIntent = new Intent(this, FindLocations.class);
        PendingIntent resultPendingIntent = PendingIntent.getActivity(this,0, resultIntent, PendingIntent.FLAG_UPDATE_CURRENT);
        mBuilder.setContentIntent(resultPendingIntent);
        // Sets an ID for the notification
        int mNotificationId = 001;
        // Gets an instance of the NotificationManager service
        NotificationManager mNotifyMgr = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        // Builds the notification and issues it.
        mNotifyMgr.notify(mNotificationId, mBuilder.build());
    }

}
