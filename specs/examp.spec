Specification Heading
=====================
Created by SONER on 15.06.2021

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Scenario Heading
----------------
bildirimler ve bilet al
* "com.android.packageinstaller:id/permission_allow_button" id li elemente tıkla
* "com.turkishairlines.mobile:id/frPrivacy_btnAccept" id li elemente tıkla
* "com.turkishairlines.mobile:id/acMain_btnBooking" id li elemente tıkla

lokasyon ayarlama
* "com.turkishairlines.mobile:id/frDashboard_tvOneWay" id li elemente tıkla
* "com.turkishairlines.mobile:id/frDashboard_llFrom" id li elemente tıkla
* "com.turkishairlines.mobile:id/frAirportSelection_etSearch" id li elemente "SAW"  değerini yaz
* "//*[@text='Istanbul, Turkey']" xpath li elemente tıkla

* "com.turkishairlines.mobile:id/frDashboard_llTo" id li elemente tıkla
* "com.turkishairlines.mobile:id/frAirportSelection_etSearch" id li elemente "ESB"  değerini yaz
*  "//*[@text='Ankara, Turkey']" xpath li elemente tıkla

//* "com.turkishairlines.mobile:id/frDashboard_rlDeparture" id li elemente tıkla

Yolcu sayısı artır
* "//*[@text='5']" xpath li elemente tıkla
* "com.turkishairlines.mobile:id/frDashboard_btnSearch" id li elemente tıkla

* "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.View" xpath li elemente tıkla
* "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]" xpath li elemente tıkla
* "com.turkishairlines.mobile:id/frFlightSearch_btnContinue" id li elemente tıkla