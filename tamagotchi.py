import flet as ft
import asyncio

def main(page: ft.Page):
    page.title = "Desktop Digital Pet"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 40
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Pet State (Variables) ---
    pet_alive = True
    hunger = 1.0      # 1.0 is completely full, 0.0 is starving
    happiness = 1.0   # 1.0 is perfectly happy, 0.0 is depressed

    # --- UI Elements ---
    # The pet's face is just a text string we will swap out!
    pet_face = ft.Text("( ^_^ )", size=100, weight=ft.FontWeight.BOLD)
    status_text = ft.Text("Your pet is doing great!", size=22, color=ft.Colors.GREEN_400)
    
    hunger_bar = ft.ProgressBar(value=hunger, width=300, color=ft.Colors.AMBER_400)
    happiness_bar = ft.ProgressBar(value=happiness, width=300, color=ft.Colors.PINK_400)

    # --- Game Logic ---
    def update_pet_ui():
        """Updates the pet's face and status based on its current stats."""
        if not pet_alive:
            pet_face.value = "( x_x )"
            status_text.value = "Oh no... your pet has passed away."
            status_text.color = ft.Colors.RED_400
            btn_feed.disabled = True
            btn_play.disabled = True
        elif hunger < 0.3 and happiness < 0.3:
            pet_face.value = "( ;_; )"
            status_text.value = "Your pet is starving and sad!"
            status_text.color = ft.Colors.RED_400
        elif hunger < 0.3:
            pet_face.value = "( O_O )"
            status_text.value = "Your pet is hungry!"
            status_text.color = ft.Colors.ORANGE_400
        elif happiness < 0.3:
            pet_face.value = "( -_- )"
            status_text.value = "Your pet is bored!"
            status_text.color = ft.Colors.BLUE_400
        else:
            pet_face.value = "( ^_^ )"
            status_text.value = "Your pet is happy!"
            status_text.color = ft.Colors.GREEN_400
        
        # Update the progress bars visually
        hunger_bar.value = hunger
        happiness_bar.value = happiness
        page.update()

    async def life_cycle():
        """The background 'Game Loop' that constantly drains stats over time."""
        nonlocal hunger, happiness, pet_alive
        
        while pet_alive:
            # Wait 2 seconds before draining stats again
            await asyncio.sleep(2) 
            
            # Decrease stats (using max() to ensure they never drop below 0.0)
            hunger = max(0.0, hunger - 0.05)
            happiness = max(0.0, happiness - 0.03)
            
            # Check for death condition
            if hunger == 0.0 and happiness == 0.0:
                pet_alive = False
            
            update_pet_ui()

    # --- Button Actions ---
    def feed_pet(e):
        nonlocal hunger
        if pet_alive:
            # Increase hunger bar, but cap it at 1.0 max
            hunger = min(1.0, hunger + 0.15)
            update_pet_ui()

    def play_with_pet(e):
        nonlocal happiness
        if pet_alive:
            # Increase happiness bar, but cap it at 1.0 max
            happiness = min(1.0, happiness + 0.15)
            update_pet_ui()

    # --- UI Layout ---
    btn_feed = ft.Button("Feed", on_click=feed_pet, color=ft.Colors.AMBER_400, height=50)
    btn_play = ft.Button("Play", on_click=play_with_pet, color=ft.Colors.PINK_400, height=50)

    controls_row = ft.Row([btn_feed, btn_play], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    
    stats_col = ft.Column(
        [
            ft.Text("Hunger", weight=ft.FontWeight.BOLD),
            hunger_bar,
            ft.Container(height=10), # Spacer
            ft.Text("Happiness", weight=ft.FontWeight.BOLD),
            happiness_bar,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Add everything to the screen
    page.add(
        ft.Text("My Digital Pet", size=32, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        pet_face,
        status_text,
        ft.Container(height=30),
        stats_col,
        ft.Container(height=30),
        controls_row
    )

    # Start the background life cycle loop!
    page.run_task(life_cycle)

ft.run(main)