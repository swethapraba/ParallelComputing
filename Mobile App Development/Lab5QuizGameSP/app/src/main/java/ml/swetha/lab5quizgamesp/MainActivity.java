package ml.swetha.lab5quizgamesp;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import static android.app.PendingIntent.getActivity;

public class MainActivity extends Activity {

    SharedPreferences sharedPref; // sharedPreferences storage
    public static final String myPreferences = "MyPrefs"; //thing that goes into shared Preferences
    String lastscores  = ""; //value to pull from sharedPreferences
    String currentscores = ""; //value to put into sharedPreferences to replace it
    int score; //make score tracker for this round while checking answers
    String[] answers ={"ada lovelace", "hedy lamarr", "grace hopper", "carol shaw", "jean sammet"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button = (Button) findViewById(R.id.submit); //define button
        button.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                score = 0;
                TextView currents = (TextView) findViewById(R.id.currentscore);
                currents.setText("This Round: " + score);
                //verify question 1
                EditText edit1 = (EditText) findViewById(R.id.answer_1);
                if(edit1.getText().toString().toLowerCase().equals(answers[0]))
                {
                    score++;

                }
                //verify question 2
                EditText edit2 = (EditText) findViewById(R.id.answer_2);
                if(edit2.getText().toString().toLowerCase().equals(answers[1]))
                {
                    score++;
                }
                //verify question 3
                EditText edit3 = (EditText) findViewById(R.id.answer_3);
                if(edit3.getText().toString().toLowerCase().equals(answers[2]))
                {
                    score++;
                }
                //verify question 4
                EditText edit4 = (EditText) findViewById(R.id.answer_4);
                if(edit4.getText().toString().toLowerCase().equals(answers[3]))
                {
                    score++;
                }
                //verify question 5
                EditText edit5 = (EditText) findViewById(R.id.answer_5);
                if(edit5.getText().toString().toLowerCase().equals(answers[4]))
                {
                    score++;
                }

                //pull old score from shared, if any
                sharedPref = getSharedPreferences("myPrefs",Context.MODE_PRIVATE);
                int value = sharedPref.getInt("myScore", 0);
              //  int value = Integer.parseInt(retrieveScore);
                //if new high score make a toast
                if(value < score)
                {
                    //make a toast
                    Context context = getApplicationContext();
                    CharSequence text = "You beat your last score!";
                    int duration = Toast.LENGTH_SHORT;
                    Toast.makeText(context, text, duration).show();
                }

                //set current score bubble
                TextView current = (TextView) findViewById(R.id.currentscore);
                current.setText("This Round: " + score);
                TextView view = (TextView) findViewById(R.id.lastscore);
                view.setText("Last Score: " + value);

                //save to shared preferences
                //make SharedPreferences object
                SharedPreferences.Editor editor = sharedPref.edit();
                editor.putInt("myScore", score);
                editor.apply();

                if(score == 5)
                {
                    //make a toast
                    Context context = getApplicationContext();
                    CharSequence text = "You win! :) ";
                    int duration = Toast.LENGTH_SHORT;
                    Toast.makeText(context, text, duration).show();
                }
            }
        });
       //button.setOnClickListener(new View.OnClickListener() {
          //  @Override
            //public void onClick(View v) {
              //  EditText edit = (EditText) findViewById(R.id.editText1); //define TextView
              //  TextView view = (TextView) findViewById(R.id.output);
              //  view.setText("Hello " + edit.getText().toString() + "!");
            //}
        //});
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}