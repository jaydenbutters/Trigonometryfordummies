import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Circle
import seaborn as sns

# Set page config
st.set_page_config(page_title="Interactive Trigonometry Calculator", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🔢 Interactive Trigonometry Calculator</h1>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a section:", [
    "Basic Trig Functions", 
    "Unit Circle Explorer", 
    "Triangle Calculator", 
    "Wave Functions", 
    "Inverse Functions"
])

if page == "Basic Trig Functions":
    st.markdown('<h2 class="section-header">Basic Trigonometric Functions</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        angle_deg = st.slider("Angle (degrees)", -360, 360, 45, 15)
        angle_rad = np.radians(angle_deg)
        
        st.subheader("Results")
        sin_val = np.sin(angle_rad)
        cos_val = np.cos(angle_rad)
        tan_val = np.tan(angle_rad) if abs(np.cos(angle_rad)) > 1e-10 else float('inf')
        
        st.write(f"**Angle:** {angle_deg}° = {angle_rad:.4f} radians")
        st.write(f"**sin({angle_deg}°):** {sin_val:.4f}")
        st.write(f"**cos({angle_deg}°):** {cos_val:.4f}")
        if abs(tan_val) < 1000:
            st.write(f"**tan({angle_deg}°):** {tan_val:.4f}")
        else:
            st.write(f"**tan({angle_deg}°):** undefined")
    
    with col2:
        # Create visualization
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        
        # Unit circle
        circle = Circle((0, 0), 1, fill=False, color='black', linewidth=2)
        ax1.add_patch(circle)
        ax1.plot([0, cos_val], [0, sin_val], 'ro-', linewidth=2, markersize=8)
        ax1.plot([cos_val, cos_val], [0, sin_val], 'b--', linewidth=2, alpha=0.7, label=f'sin = {sin_val:.3f}')
        ax1.plot([0, cos_val], [0, 0], 'g--', linewidth=2, alpha=0.7, label=f'cos = {cos_val:.3f}')
        ax1.set_xlim(-1.5, 1.5)
        ax1.set_ylim(-1.5, 1.5)
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.set_title(f'Unit Circle - Angle: {angle_deg}°')
        ax1.legend()
        
        # Sine function
        x = np.linspace(-2*np.pi, 2*np.pi, 1000)
        ax2.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
        ax2.axvline(angle_rad, color='red', linestyle='--', alpha=0.7)
        ax2.plot(angle_rad, sin_val, 'ro', markersize=10)
        ax2.set_title('Sine Function')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlabel('Angle (radians)')
        ax2.set_ylabel('sin(x)')
        ax2.legend()
        
        # Cosine function
        ax3.plot(x, np.cos(x), 'g-', linewidth=2, label='cos(x)')
        ax3.axvline(angle_rad, color='red', linestyle='--', alpha=0.7)
        ax3.plot(angle_rad, cos_val, 'ro', markersize=10)
        ax3.set_title('Cosine Function')
        ax3.grid(True, alpha=0.3)
        ax3.set_xlabel('Angle (radians)')
        ax3.set_ylabel('cos(x)')
        ax3.legend()
        
        # Tangent function
        x_tan = np.linspace(-2*np.pi, 2*np.pi, 1000)
        y_tan = np.tan(x_tan)
        # Remove discontinuities for better plotting
        y_tan[np.abs(y_tan) > 10] = np.nan
        ax4.plot(x_tan, y_tan, 'orange', linewidth=2, label='tan(x)')
        ax4.axvline(angle_rad, color='red', linestyle='--', alpha=0.7)
        if abs(tan_val) < 10:
            ax4.plot(angle_rad, tan_val, 'ro', markersize=10)
        ax4.set_title('Tangent Function')
        ax4.set_ylim(-5, 5)
        ax4.grid(True, alpha=0.3)
        ax4.set_xlabel('Angle (radians)')
        ax4.set_ylabel('tan(x)')
        ax4.legend()
        
        plt.tight_layout()
        st.pyplot(fig)

elif page == "Unit Circle Explorer":
    st.markdown('<h2 class="section-header">Unit Circle Explorer</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Interactive Controls")
        angle_deg = st.slider("Angle (degrees)", 0, 360, 45, 5)
        show_reference = st.checkbox("Show reference angles", True)
        show_quadrants = st.checkbox("Show quadrant labels", True)
        
        angle_rad = np.radians(angle_deg)
        sin_val = np.sin(angle_rad)
        cos_val = np.cos(angle_rad)
        
        # Quadrant information
        if 0 <= angle_deg <= 90:
            quadrant = "I"
        elif 90 < angle_deg <= 180:
            quadrant = "II"
        elif 180 < angle_deg <= 270:
            quadrant = "III"
        else:
            quadrant = "IV"
        
        st.subheader("Information")
        st.write(f"**Quadrant:** {quadrant}")
        st.write(f"**Coordinates:** ({cos_val:.3f}, {sin_val:.3f})")
        
        # Special angles
        special_angles = {
            0: "0°", 30: "30°", 45: "45°", 60: "60°", 90: "90°",
            120: "120°", 135: "135°", 150: "150°", 180: "180°",
            210: "210°", 225: "225°", 240: "240°", 270: "270°",
            300: "300°", 315: "315°", 330: "330°", 360: "360°"
        }
        
        if angle_deg in special_angles:
            st.success(f"Special angle: {special_angles[angle_deg]}")
    
    with col2:
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        
        # Draw unit circle
        circle = Circle((0, 0), 1, fill=False, color='black', linewidth=3)
        ax.add_patch(circle)
        
        # Draw axes
        ax.axhline(y=0, color='black', linewidth=1, alpha=0.5)
        ax.axvline(x=0, color='black', linewidth=1, alpha=0.5)
        
        # Draw angle line
        ax.plot([0, cos_val], [0, sin_val], 'red', linewidth=4, label=f'{angle_deg}°')
        ax.plot(cos_val, sin_val, 'ro', markersize=15)
        
        # Draw projections
        ax.plot([cos_val, cos_val], [0, sin_val], 'blue', linewidth=3, alpha=0.7, 
                label=f'sin({angle_deg}°) = {sin_val:.3f}')
        ax.plot([0, cos_val], [0, 0], 'green', linewidth=3, alpha=0.7, 
                label=f'cos({angle_deg}°) = {cos_val:.3f}')
        
        # Add quadrant labels
        if show_quadrants:
            ax.text(0.7, 0.7, 'I', fontsize=20, ha='center', va='center', 
                   bbox=dict(boxstyle="circle", facecolor='lightblue', alpha=0.5))
            ax.text(-0.7, 0.7, 'II', fontsize=20, ha='center', va='center',
                   bbox=dict(boxstyle="circle", facecolor='lightgreen', alpha=0.5))
            ax.text(-0.7, -0.7, 'III', fontsize=20, ha='center', va='center',
                   bbox=dict(boxstyle="circle", facecolor='lightyellow', alpha=0.5))
            ax.text(0.7, -0.7, 'IV', fontsize=20, ha='center', va='center',
                   bbox=dict(boxstyle="circle", facecolor='lightcoral', alpha=0.5))
        
        # Add special angle markers
        if show_reference:
            special_angles_rad = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 
                                2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi,
                                7*np.pi/6, 5*np.pi/4, 4*np.pi/3, 3*np.pi/2,
                                5*np.pi/3, 7*np.pi/4, 11*np.pi/6]
            
            for angle in special_angles_rad:
                x, y = np.cos(angle), np.sin(angle)
                ax.plot(x, y, 'ko', markersize=6, alpha=0.6)
        
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_title(f'Unit Circle - Angle: {angle_deg}° (Quadrant {quadrant})', fontsize=16)
        
        plt.tight_layout()
        st.pyplot(fig)

elif page == "Triangle Calculator":
    st.markdown('<h2 class="section-header">Right Triangle Calculator</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Triangle Parameters")
        
        calc_type = st.radio("Calculate using:", ["Angle and Hypotenuse", "Two Sides", "Angle and Adjacent", "Angle and Opposite"])
        
        if calc_type == "Angle and Hypotenuse":
            angle = st.slider("Angle (degrees)", 1, 89, 30)
            hypotenuse = st.number_input("Hypotenuse", min_value=0.1, value=10.0)
            
            angle_rad = np.radians(angle)
            opposite = hypotenuse * np.sin(angle_rad)
            adjacent = hypotenuse * np.cos(angle_rad)
            
        elif calc_type == "Two Sides":
            opposite = st.number_input("Opposite side", min_value=0.1, value=5.0)
            adjacent = st.number_input("Adjacent side", min_value=0.1, value=8.0)
            
            hypotenuse = np.sqrt(opposite**2 + adjacent**2)
            angle_rad = np.arctan(opposite / adjacent)
            angle = np.degrees(angle_rad)
            
        elif calc_type == "Angle and Adjacent":
            angle = st.slider("Angle (degrees)", 1, 89, 30)
            adjacent = st.number_input("Adjacent side", min_value=0.1, value=8.0)
            
            angle_rad = np.radians(angle)
            opposite = adjacent * np.tan(angle_rad)
            hypotenuse = adjacent / np.cos(angle_rad)
            
        else:  # Angle and Opposite
            angle = st.slider("Angle (degrees)", 1, 89, 30)
            opposite = st.number_input("Opposite side", min_value=0.1, value=5.0)
            
            angle_rad = np.radians(angle)
            adjacent = opposite / np.tan(angle_rad)
            hypotenuse = opposite / np.sin(angle_rad)
        
        st.subheader("Results")
        st.write(f"**Angle A:** {angle:.2f}°")
        st.write(f"**Angle B:** {90-angle:.2f}°")
        st.write(f"**Opposite:** {opposite:.3f}")
        st.write(f"**Adjacent:** {adjacent:.3f}")
        st.write(f"**Hypotenuse:** {hypotenuse:.3f}")
        st.write(f"**Area:** {0.5 * opposite * adjacent:.3f}")
        st.write(f"**Perimeter:** {opposite + adjacent + hypotenuse:.3f}")
    
    with col2:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        # Draw triangle
        triangle_x = [0, adjacent, 0, 0]
        triangle_y = [0, 0, opposite, 0]
        ax1.plot(triangle_x, triangle_y, 'b-', linewidth=3)
        
        # Add labels
        ax1.text(adjacent/2, -0.5, f'Adjacent = {adjacent:.2f}', ha='center', fontsize=12)
        ax1.text(-1, opposite/2, f'Opposite = {opposite:.2f}', ha='center', rotation=90, fontsize=12)
        ax1.text(adjacent/2 + 0.5, opposite/2 + 0.5, f'Hypotenuse = {hypotenuse:.2f}', 
                ha='center', rotation=-np.degrees(angle_rad), fontsize=12)
        ax1.text(1, 0.5, f'{angle:.1f}°', ha='center', fontsize=12)
        
        # Right angle marker
        square_size = min(adjacent, opposite) * 0.1
        square_x = [0, square_size, square_size, 0, 0]
        square_y = [0, 0, square_size, square_size, 0]
        ax1.plot(square_x, square_y, 'r-', linewidth=2)
        
        ax1.set_xlim(-2, adjacent + 2)
        ax1.set_ylim(-2, opposite + 2)
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.set_title('Right Triangle Visualization')
        
        # Trigonometric ratios visualization
        angles = np.linspace(1, 89, 100)
        if calc_type in ["Angle and Hypotenuse", "Angle and Adjacent", "Angle and Opposite"]:
            # Show how ratios change with angle
            angles_rad = np.radians(angles)
            if calc_type == "Angle and Hypotenuse":
                opposites = hypotenuse * np.sin(angles_rad)
                adjacents = hypotenuse * np.cos(angles_rad)
                ax2.plot(angles, opposites, 'r-', label='Opposite', linewidth=2)
                ax2.plot(angles, adjacents, 'g-', label='Adjacent', linewidth=2)
                ax2.axhline(hypotenuse, color='b', linestyle='--', label=f'Hypotenuse = {hypotenuse:.2f}')
            elif calc_type == "Angle and Adjacent":
                opposites = adjacent * np.tan(angles_rad)
                hypotenuses = adjacent / np.cos(angles_rad)
                ax2.plot(angles, opposites, 'r-', label='Opposite', linewidth=2)
                ax2.plot(angles, hypotenuses, 'b-', label='Hypotenuse', linewidth=2)
                ax2.axhline(adjacent, color='g', linestyle='--', label=f'Adjacent = {adjacent:.2f}')
            else:  # Angle and Opposite
                adjacents = opposite / np.tan(angles_rad)
                hypotenuses = opposite / np.sin(angles_rad)
                ax2.plot(angles, adjacents, 'g-', label='Adjacent', linewidth=2)
                ax2.plot(angles, hypotenuses, 'b-', label='Hypotenuse', linewidth=2)
                ax2.axhline(opposite, color='r', linestyle='--', label=f'Opposite = {opposite:.2f}')
            
            ax2.axvline(angle, color='black', linestyle=':', alpha=0.7, label=f'Current angle = {angle}°')
            ax2.set_xlabel('Angle (degrees)')
            ax2.set_ylabel('Side Length')
            ax2.set_title('How Side Lengths Change with Angle')
        else:
            # For "Two Sides", show trig function values
            sin_vals = np.sin(angles_rad)
            cos_vals = np.cos(angles_rad)
            tan_vals = np.tan(angles_rad)
            
            ax2.plot(angles, sin_vals, 'r-', label='sin', linewidth=2)
            ax2.plot(angles, cos_vals, 'g-', label='cos', linewidth=2)
            ax2.plot(angles, tan_vals, 'b-', label='tan', linewidth=2)
            ax2.axvline(angle, color='black', linestyle=':', alpha=0.7, label=f'Current angle = {angle:.1f}°')
            ax2.set_xlabel('Angle (degrees)')
            ax2.set_ylabel('Function Value')
            ax2.set_title('Trigonometric Functions')
            ax2.set_ylim(0, 3)
        
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        plt.tight_layout()
        st.pyplot(fig)

elif page == "Wave Functions":
    st.markdown('<h2 class="section-header">Trigonometric Wave Functions</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Wave Parameters")
        wave_type = st.selectbox("Wave Type", ["Sine", "Cosine", "Tangent"])
        amplitude = st.slider("Amplitude (A)", 0.1, 5.0, 1.0, 0.1)
        frequency = st.slider("Frequency (f)", 0.1, 3.0, 1.0, 0.1)
        phase = st.slider("Phase Shift (φ) degrees", -180, 180, 0, 15)
        vertical_shift = st.slider("Vertical Shift (D)", -2.0, 2.0, 0.0, 0.1)
        
        phase_rad = np.radians(phase)
        
        st.subheader("Wave Equation")
        if wave_type == "Sine":
            st.latex(f"y = {amplitude} \\sin({frequency}x + {phase_rad:.2f}) + {vertical_shift}")
        elif wave_type == "Cosine":
            st.latex(f"y = {amplitude} \\cos({frequency}x + {phase_rad:.2f}) + {vertical_shift}")
        else:
            st.latex(f"y = {amplitude} \\tan({frequency}x + {phase_rad:.2f}) + {vertical_shift}")
        
        st.subheader("Properties")
        period = 2 * np.pi / frequency
        st.write(f"**Period:** {period:.2f}")
        st.write(f"**Amplitude:** {amplitude}")
        st.write(f"**Frequency:** {frequency}")
        st.write(f"**Phase Shift:** {phase}° = {phase_rad:.2f} rad")
        st.write(f"**Vertical Shift:** {vertical_shift}")
    
    with col2:
        x = np.linspace(-4*np.pi, 4*np.pi, 2000)
        
        if wave_type == "Sine":
            y = amplitude * np.sin(frequency * x + phase_rad) + vertical_shift
            base_y = np.sin(x)
        elif wave_type == "Cosine":
            y = amplitude * np.cos(frequency * x + phase_rad) + vertical_shift
            base_y = np.cos(x)
        else:
            y = amplitude * np.tan(frequency * x + phase_rad) + vertical_shift
            base_y = np.tan(x)
            # Limit tangent values for better visualization
            y = np.clip(y, -10, 10)
            base_y = np.clip(base_y, -10, 10)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Modified wave
        ax1.plot(x, y, 'b-', linewidth=3, label=f'Modified {wave_type}')
        ax1.axhline(vertical_shift, color='red', linestyle='--', alpha=0.7, label=f'Vertical Shift = {vertical_shift}')
        ax1.axhline(vertical_shift + amplitude, color='green', linestyle=':', alpha=0.7, label=f'Max = {vertical_shift + amplitude:.2f}')
        ax1.axhline(vertical_shift - amplitude, color='green', linestyle=':', alpha=0.7, label=f'Min = {vertical_shift - amplitude:.2f}')
        
        ax1.set_xlim(-4*np.pi, 4*np.pi)
        if wave_type != "Tangent":
            ax1.set_ylim(-6, 6)
        else:
            ax1.set_ylim(-10, 10)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_title(f'Modified {wave_type} Wave')
        ax1.set_xlabel('x (radians)')
        ax1.set_ylabel('y')
        
        # Comparison with base function
        ax2.plot(x, base_y, 'gray', linewidth=2, alpha=0.5, label=f'Base {wave_type}')
        ax2.plot(x, y, 'b-', linewidth=3, label=f'Modified {wave_type}')
        
        ax2.set_xlim(-4*np.pi, 4*np.pi)
        if wave_type != "Tangent":
            ax2.set_ylim(-6, 6)
        else:
            ax2.set_ylim(-10, 10)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        ax2.set_title('Comparison: Base vs Modified Function')
        ax2.set_xlabel('x (radians)')
        ax2.set_ylabel('y')
        
        plt.tight_layout()
        st.pyplot(fig)

else:  # Inverse Functions
    st.markdown('<h2 class="section-header">Inverse Trigonometric Functions</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        function_type = st.selectbox("Function", ["arcsin", "arccos", "arctan"])
        
        if function_type == "arcsin":
            input_val = st.slider("Input value", -1.0, 1.0, 0.5, 0.01)
            result_rad = np.arcsin(input_val)
            domain_text = "[-1, 1]"
            range_text = "[-π/2, π/2]"
        elif function_type == "arccos":
            input_val = st.slider("Input value", -1.0, 1.0, 0.5, 0.01)
            result_rad = np.arccos(input_val)
            domain_text = "[-1, 1]"
            range_text = "[0, π]"
        else:  # arctan
            input_val = st.slider("Input value", -10.0, 10.0, 1.0, 0.1)
            result_rad = np.arctan(input_val)
            domain_text = "(-∞, ∞)"
            range_text = "(-π/2, π/2)"
        
        result_deg = np.degrees(result_rad)
        
        st.subheader("Results")
        st.write(f"**Input:** {input_val}")
        st.write(f"**{function_type}({input_val}):** {result_rad:.4f} radians")
        st.write(f"**{function_type}({input_val}):** {result_deg:.2f}°")
        
        st.subheader("Function Properties")
        st.write(f"**Domain:** {domain_text}")
        st.write(f"**Range:** {range_text}")
        
        # Verification
        st.subheader("Verification")
        if function_type == "arcsin":
            verification = np.sin(result_rad)
            st.write(f"sin({result_rad:.4f}) = {verification:.4f}")
        elif function_type == "arccos":
            verification = np.cos(result_rad)
            st.write(f"cos({result_rad:.4f}) = {verification:.4f}")
        else:
            verification = np.tan(result_rad)
            st.write(f"tan({result_rad:.4f}) = {verification:.4f}")
    
    with col2:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        
        # Plot the inverse function
        if function_type == "arcsin":
            x_vals = np.linspace(-1, 1, 1000)
            y_vals = np.arcsin(x_vals)
            ax1.plot(x_vals, y_vals, 'b-', linewidth=3, label='arcsin(x)')
            ax1.set_ylim(-np.pi/2 - 0.5, np.pi/2 + 0.5)
        elif function_type == "arccos":
            x_vals = np.linspace(-1, 1, 1000)
            y_vals = np.arccos(x_vals)
            ax1.plot(x_vals, y_vals, 'g-', linewidth=3, label='arccos(x)')
            ax1.set_ylim(-0.5, np.pi + 0.5)
        else:
            x_vals = np.linspace(-10, 10, 1000)
            y_vals = np.arctan(x_vals)
            ax1.plot(x_vals, y_vals, 'r-', linewidth=3, label='arctan(x)')
            ax1.axhline(np.pi/2, color='gray', linestyle='--', alpha=0.5, label='y = π/2')
            ax1.axhline(-np.pi/2, color='gray', linestyle='--', alpha=0.5, label='y = -π/2')
            ax1.set_ylim(-np.pi/2 - 0.5, np.pi/2 + 0.5)
        
        ax1.plot(input_val, result_rad, 'ro', markersize=10)
        ax1.axvline(input_val, color='red', linestyle='--', alpha=0.7)
        ax1.axhline(result_rad, color='red', linestyle='--', alpha=0.7)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_title(f'{function_type}(x)')
        ax1.set_xlabel('x')
        ax1.set_ylabel('y (radians)')
        
        # Plot the corresponding regular trig function
        x_trig = np.linspace(-2*np.pi, 2*np.pi, 1000)
        if function_type == "arcsin":
            y_trig = np.sin(x_trig)
            ax2.plot(x_trig, y_trig, 'b-', linewidth=2, alpha=0.7, label='sin(x)')
            # Highlight the principal domain
            x_principal = np.linspace(-np.pi/2, np.pi/2, 100)
            y_principal = np.sin(x_principal)
            ax2.plot(x_principal, y_principal, 'b-', linewidth=4, label='Principal branch')
        elif function_type == "arccos":
            y_trig = np.cos(x_trig)
            ax2.plot(x_trig, y_trig, 'g-', linewidth=2, alpha=0.7, label='cos(x)')
            x_principal = np.linspace(0, np.pi, 100)
            y_principal = np.cos(x_principal)
            ax2.plot(x_principal, y_principal, 'g-', linewidth=4, label='Principal branch')
        else:
            y_trig = np.tan(x_trig)
            y_trig[np.abs(y_trig) > 10] = np.nan  # Remove discontinuities
            ax2.plot(x_trig, y_trig, 'r-', linewidth=2, alpha=0.7, label='tan(x)')
            x_principal = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 100)
            y_principal = np.tan(x_principal)
            ax2.plot(x_principal, y_principal, 'r-', linewidth=4, label='Principal branch')
        
        ax2.plot(result_rad, input_val, 'ro', markersize=10)
        ax2.axvline(result_rad, color='red', linestyle='--', alpha=0.7)
        ax2.axhline(input_val, color='red', linestyle='--', alpha=0.7)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        ax2.set_title(f'Corresponding {function_type[3:]}(x) function')
        ax2.set_xlabel('x (radians)')
        ax2.set_ylabel('y')
        ax2.set_ylim(-3, 3)
        
        # Unit circle representation
        circle = Circle((0, 0), 1, fill=False, color='black', linewidth=2)
        ax3.add_patch(circle)
        
        if function_type in ["arcsin", "arccos"]:
            # For arcsin and arccos, show the angle on unit circle
            angle_for_circle = result_rad if function_type == "arcsin" else result_rad
            x_circle = np.cos(angle_for_circle)
            y_circle = np.sin(angle_for_circle)
            
            ax3.plot([0, x_circle], [0, y_circle], 'ro-', linewidth=3, markersize=8)
            ax3.plot([x_circle, x_circle], [0, y_circle], 'b--', linewidth=2, alpha=0.7)
            ax3.plot([0, x_circle], [0, 0], 'g--', linewidth=2, alpha=0.7)
            
            if function_type == "arcsin":
                ax3.text(0.1, 0.1, f'arcsin({input_val:.2f}) = {result_deg:.1f}°', 
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
            else:
                ax3.text(0.1, 0.1, f'arccos({input_val:.2f}) = {result_deg:.1f}°', 
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
        else:
            # For arctan, show the slope
            ax3.plot([0, 1], [0, input_val], 'ro-', linewidth=3, markersize=8, 
                    label=f'slope = {input_val:.2f}')
            ax3.text(0.1, 0.1, f'arctan({input_val:.2f}) = {result_deg:.1f}°', 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
        
        ax3.set_xlim(-1.5, 1.5)
        ax3.set_ylim(-1.5, 1.5)
        ax3.set_aspect('equal')
        ax3.grid(True, alpha=0.3)
        ax3.set_title('Unit Circle Representation')
        
        # Comparison table of values
        ax4.axis('off')
        
        if function_type == "arcsin":
            special_values = [
                [-1, -90], [-0.866, -60], [-0.707, -45], [-0.5, -30], 
                [0, 0], [0.5, 30], [0.707, 45], [0.866, 60], [1, 90]
            ]
            headers = ['x', 'arcsin(x) (°)']
        elif function_type == "arccos":
            special_values = [
                [-1, 180], [-0.866, 150], [-0.707, 135], [-0.5, 120], 
                [0, 90], [0.5, 60], [0.707, 45], [0.866, 30], [1, 0]
            ]
            headers = ['x', 'arccos(x) (°)']
        else:
            special_values = [
                [-1.732, -60], [-1, -45], [-0.577, -30], [0, 0], 
                [0.577, 30], [1, 45], [1.732, 60], [2.747, 70]
            ]
            headers = ['x', 'arctan(x) (°)']
        
        # Create table
        table_data = []
        for val, deg in special_values:
            if abs(val - input_val) < 0.1:
                table_data.append([f"→ {val:.3f}", f"→ {deg}°"])
            else:
                table_data.append([f"{val:.3f}", f"{deg}°"])
        
        table = ax4.table(cellText=table_data, colLabels=headers,
                         cellLoc='center', loc='center',
                         bbox=[0, 0, 1, 1])
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)
        
        # Highlight current value row
        for i, (val, deg) in enumerate(special_values):
            if abs(val - input_val) < 0.1:
                for j in range(2):
                    table[(i+1, j)].set_facecolor('#ffcccc')
        
        ax4.set_title('Special Values Reference')
        
        plt.tight_layout()
        st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("### 📚 Quick Reference")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Basic Identities:**")
    st.markdown("• sin²θ + cos²θ = 1")
    st.markdown("• tan θ = sin θ / cos θ")
    st.markdown("• 1 + tan²θ = sec²θ")

with col2:
    st.markdown("**Special Angles:**")
    st.markdown("• sin(30°) = 1/2, cos(30°) = √3/2")
    st.markdown("• sin(45°) = √2/2, cos(45°) = √2/2")
    st.markdown("• sin(60°) = √3/2, cos(60°) = 1/2")

with col3:
    st.markdown("**Unit Circle:**")
    st.markdown("• (cos θ, sin θ) = point on circle")
    st.markdown("• Period: 2π radians = 360°")
    st.markdown("• Quadrants determine sign")
