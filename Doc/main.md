``` mermaid
graph TD
    A[main] --> B[YourMainWindowClass_init]
    B --> C[apply_actions_to_buttons]
    C --> D[button_controller]
    B --> E[start_program]
    E --> F[stack_controller]
    A --> G[start_program]
    A --> H[sys_exit]
```