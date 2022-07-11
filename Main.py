import streamlit as st
import Gear.Gear as gear
import Players.Player as player
import Players.Monsters as monsters
import Dpsformulas.Magic as dps_ma
import Dpsformulas.Melee as dps_me
import Dpsformulas.Ranged as dps_ra


def main(style):
    styles = {"Melee": "dps_me.Melee_dps_calc()", "Ranged": "dps_ra.Ranged_dps_calc()", "Magic": "dps_ma.Magic_dps_calc()"}
    eval(styles[style])


if __name__ == "__main__":
    atk_style = st.sidebar.selectbox("Select attack style", ("Melee", "Ranged", "Magic"))
    main(atk_style)



