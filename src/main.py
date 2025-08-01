import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




def getPrintScreenKnowledgeErrors(data, cols):
    errors_list = ["didn't know", "couldn't find", "no attempt", "idk", "incorrect"]

    pattern = '|'.join(errors_list)

    task_4_errors_count = data[cols[0]].str.contains(pattern, case=False, na=False)
    num_errors_task_4 = task_4_errors_count.sum()
    num_task_4_responses = data[cols[0]].count()
    task_5_errors_count = data[cols[1]].str.contains(pattern, case=False, na=False)
    num_errors_task_5 = task_5_errors_count.sum()
    num_task_5_responses = data[cols[1]].count()

    return {
        "num_errors_task_4": num_errors_task_4,
        "num_task_4_responses": num_task_4_responses,
        "num_errors_task_5": num_errors_task_5,
        "num_task_5_responses": num_task_5_responses
    }


def getPrintScreenRulesErrors(data, cols):
    errors_list = ["was able to get", "First did"]
    pattern = '|'.join(errors_list)

    task_4_errors_count = data[cols[0]].str.contains(pattern, case=False, na=False)
    num_errors_task_4 = task_4_errors_count.sum()
    num_task_4_responses = data[cols[0]].count()
    task_5_errors_count = data[cols[1]].str.contains(pattern, case=False, na=False)
    num_errors_task_5 = task_5_errors_count.sum()
    num_task_5_responses = data[cols[1]].count()


    return {
        "num_errors_task_4": num_errors_task_4,
        "num_task_4_responses": num_task_4_responses,
        "num_errors_task_5": num_errors_task_5,
        "num_task_5_responses": num_task_5_responses
    }


def graphErrors(print_screen_knowledge_errors, print_screen_rules_errors):
    # Set up seaborn style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (14, 6)
    
    # Prepare data for knowledge errors
    knowledge_data = pd.DataFrame({
        'Task': ['Task 4', 'Task 4', 'Task 5', 'Task 5'],
        'Type': ['Errors', 'Total Responses', 'Errors', 'Total Responses'],
        'Count': [
            print_screen_knowledge_errors["num_errors_task_4"],
            print_screen_knowledge_errors["num_task_4_responses"],
            print_screen_knowledge_errors["num_errors_task_5"],
            print_screen_knowledge_errors["num_task_5_responses"]
        ]
    })
    
    # Prepare data for rules errors
    rules_data = pd.DataFrame({
        'Task': ['Task 4', 'Task 4', 'Task 5', 'Task 5'],
        'Type': ['Errors', 'Total Responses', 'Errors', 'Total Responses'],
        'Count': [
            print_screen_rules_errors["num_errors_task_4"],
            print_screen_rules_errors["num_task_4_responses"],
            print_screen_rules_errors["num_errors_task_5"],
            print_screen_rules_errors["num_task_5_responses"]
        ]
    })
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Knowledge errors plot
    sns.barplot(data=knowledge_data, x='Task', y='Count', hue='Type', 
                ax=ax1, palette=['coral', 'skyblue'])
    ax1.set_title('Knowledge Errors vs Total Responses', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Count', fontsize=12)
    ax1.set_xlabel('Task', fontsize=12)
    ax1.figure.savefig('knowledge_errors.jpg', dpi=300, bbox_inches='tight')

    
    # Add value labels on bars
    for container in ax1.containers:
        ax1.bar_label(container, fmt='%d')
    
    # Rules errors plot
    sns.barplot(data=rules_data, x='Task', y='Count', hue='Type', 
                ax=ax2, palette=['orange', 'lightgreen'])
    ax2.set_title('Rules Errors vs Total Responses', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Count', fontsize=12)
    ax2.set_xlabel('Task', fontsize=12)
    ax2.figure.savefig('rules_errors.jpg', dpi=300, bbox_inches='tight')
    # Add value labels on bars
    for container in ax2.containers:
        ax2.bar_label(container, fmt='%d')
    
    plt.tight_layout()
    plt.show()
    
    # Print summary statistics
    print("\n=== KNOWLEDGE ERRORS SUMMARY ===")
    k4_err = print_screen_knowledge_errors["num_errors_task_4"]
    k4_tot = print_screen_knowledge_errors["num_task_4_responses"]
    k5_err = print_screen_knowledge_errors["num_errors_task_5"]
    k5_tot = print_screen_knowledge_errors["num_task_5_responses"]
    
    print(f"Task 4: {k4_err}/{k4_tot} errors ({k4_err/k4_tot*100:.1f}%)")
    print(f"Task 5: {k5_err}/{k5_tot} errors ({k5_err/k5_tot*100:.1f}%)")
    
    print("\n=== RULES ERRORS SUMMARY ===")
    r4_err = print_screen_rules_errors["num_errors_task_4"]
    r4_tot = print_screen_rules_errors["num_task_4_responses"]
    r5_err = print_screen_rules_errors["num_errors_task_5"]
    r5_tot = print_screen_rules_errors["num_task_5_responses"]
    
    print(f"Task 4: {r4_err}/{r4_tot} errors ({r4_err/r4_tot*100:.1f}%)")
    print(f"Task 5: {r5_err}/{r5_tot} errors ({r5_err/r5_tot*100:.1f}%)")

    



def main():
    print("Hello, World!")

    dir_path = os.path.dirname(__file__)
    print(dir_path)
    data_path = os.path.join(dir_path, "..", "data", "data.csv")
    print(data_path)
    data = pd.read_csv(data_path)
    print(data.head())

    cols = ["Task 4 (screenshot to clipboard)", "Task 5 (screenshot full screen"]

    print_screen_knowledge_errors = getPrintScreenKnowledgeErrors(data, cols)
    print_screen_rules_errors = getPrintScreenRulesErrors(data, cols)

    graphErrors(print_screen_knowledge_errors, print_screen_rules_errors)



if __name__ == "__main__":
    main()